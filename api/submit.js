// Saves the site's three forms (mailing list signup, dealer install quote, contact message)
// into the form_entries table in Neon. DATABASE_URL uses the insert-only web_forms role.
import { neon } from '@neondatabase/serverless';

const sql = neon(process.env.DATABASE_URL);
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

const text = (v, max) => (typeof v === 'string' ? v.trim().slice(0, max) : '');

function clean(kind, b) {
  if (kind === 'signup') {
    const email = text(b.email, 254);
    if (!EMAIL.test(email)) return { error: 'Enter an email address like you@example.com.' };
    return { email };
  }
  if (kind === 'contact') {
    const row = { name: text(b.name, 120), email: text(b.email, 254), phone: text(b.phone, 40), message: text(b.message, 5000) };
    if (!row.name || !EMAIL.test(row.email) || !row.message) return { error: 'Please fill in your name, email and message.' };
    row.details = { department: text(b.department, 120) };
    return row;
  }
  // quote: "contact" is a phone number or an email address
  const name = text(b.name, 120);
  const contact = text(b.contact, 254);
  const shops = (Array.isArray(b.shops) ? b.shops : []).map((s) => text(s, 160)).filter(Boolean).slice(0, 10);
  if (!name || !contact || !shops.length) return { error: 'Pick at least one shop and add your first name and a phone or email.' };
  return {
    name,
    email: contact.includes('@') ? contact : '',
    phone: contact.includes('@') ? '' : contact,
    details: { shops, car: text(b.car, 120), system: text(b.system, 40), zip: text(b.zip, 10) },
  };
}

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false, error: 'Use POST.' });
  }
  const b = req.body && typeof req.body === 'object' ? req.body : {};
  if (b.website) return res.status(200).json({ ok: true }); // honeypot: bots fill the hidden field
  if (!['signup', 'quote', 'contact'].includes(b.kind)) return res.status(400).json({ ok: false, error: 'Unknown form.' });

  const row = clean(b.kind, b);
  if (row.error) return res.status(400).json({ ok: false, error: row.error });

  let page = '';
  try { page = new URL(req.headers.referer || '').pathname.slice(0, 300); } catch { page = ''; }

  try {
    await sql`
      INSERT INTO form_entries (kind, name, email, phone, message, details, page, user_agent)
      VALUES (${b.kind}, ${row.name || null}, ${row.email || null}, ${row.phone || null}, ${row.message || null},
              ${JSON.stringify(row.details || {})}::jsonb, ${page || null}, ${text(req.headers['user-agent'], 300) || null})`;
  } catch (err) {
    console.error('form_entries insert failed', err);
    return res.status(500).json({ ok: false, error: 'We could not save that. Please call (800) 852-3228.' });
  }
  return res.status(200).json({ ok: true });
}
