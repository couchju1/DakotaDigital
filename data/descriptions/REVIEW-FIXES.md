# Description fixes: review

Second pass on product descriptions: the copy lint (`npm run lint:copy`, `scripts/lint-descriptions.mjs`), rewrites for every product page that had none, and fixes for rewrites that carried over original wording. Same fact rules as the first run: every fact comes from the product's own description, spec tabs, options, versions or title.

## Flagged for a human look

- **191 rewrites are under 90 words on purpose.** Their pages don't have enough facts to reach 90 words without padding (parts lists, single senders, relays, transmitters, discontinued placeholders). Each file says why in a `short:` front-matter line, and the lint allows it. The full list is at the end of this file.
- **Three discontinued placeholders** (p600, p1105, p1127) only say the product is no longer listed. Their rewrites say the same in new words.
- **XMT-6 (p80):** the page title and description say 6-button, but the buy-box item name says "10 Button Replacement Transmitter". The rewrite says 6-button.
- **XMT-4 (p81)** and **SEN-3111 (p330)** and **SEN-201 (p983)** have no description on the live page. Their rewrites use only the title, item names and (for SEN-3111) the HLY-3111 page that requires it.
- **LED tail lights:** seven pages (1960-65 Impalas, 1967 Impala, 1975-76 Caprice and the 1971-73 Mustang) carry the note "LAT-NR161 - Includes product located under tail light assembly". It's vague, and on the Mustang page it names a different part number. The rewrites repeat it as "the page notes that the LAT-NR161 includes a part located under the tail light assembly".
- **Lists that didn't come through the crawl:** several pages (CMD-10K, CMD-4000, PAC-3500, VCM-101, VCM-200, MLX-9000, MVX-2002, HLY-301 and others) say "Features include:" or "Includes:" and the list itself isn't in the saved page data. Those rewrites only use what was readable; the live pages may have more to say.
- **Automotive Technical Manuals (p393):** the original note about switching from Firefox to Internet Explorer to download manuals is out of date and was left out.
- **VHX-1200 (p880):** its original description is cut off mid-sentence ("Measuring in at 16..."), so the size isn't in the rewrite.
- **Known problems from the task, confirmed:** p1053, p1368, p1202, p1425 and p1159 had no rewrite at all, so their pages showed the original copy (that is where "high-zoot", "streamline" and the semicolons came from). The "over 160 words" and "!" pages were also original copy on unrewritten pages. All are rewritten now.
- **Boilerplate reworded in 175 earlier rewrites:** the first run reused the cleaned-up series paragraphs nearly word for word (for example "Every RTX housing is CNC machined, and the electronics are designed and built in-house"). The lint flags any 12-word run shared with the original, so those sentences were reworded with the same facts. REVIEW.md still shows the older wording for those products.

## Lint results

| Check | Before | After |
| --- | --- | --- |
| missing | 353 | 0 |
| empty | 0 | 0 |
| words | 0 | 0 |
| punctuation | 0 | 0 |
| banned | 0 | 0 |
| carryover | 160 | 0 |
| duplicateOpening | 0 | 0 |
| schema | 0 | 0 |
| unknownProduct | 0 | 0 |

"Before" is the first lint run on the 410 earlier rewrites. The 353 missing products were original copy on the live pages; in that copy, 39 ran over 160 words, 86 had an exclamation point, 35 had a semicolon, 18 used a banned word, 142 were under 60 words and 6 had no description at all.

Lint fix during the work: the sentence splitter cut sentences at decimals like "0.1", which made two different openings look identical. It now ends a sentence only at a period or question mark followed by a space or the end.

## VHX-1022 (p937) source check

| Fact in the rewrite | Found in | What the page says | Result |
| --- | --- | --- | --- |
| 10 ft harnesses | Specifications tab, Included Sensors | water temp and oil pressure sensors "with a 10 ft harness"; speed sensor "Replaces GM style speedometer cables with a 10 ft harness" | Kept |
| 0-60 timer | Specifications tab, Performance Meters | "0- 60 MPH Timer (0- 100 kmh)" | Kept |
| Blue, red or white lighting | Options (buy box) | Color: Blue, Red, White | Kept |

All three facts are on the page. Nothing was removed.

## Spot check: 15 random earlier rewrites

Picked at random (seed 20261031) from the 410 earlier rewrites, leaving out the products named in the task. Every number, measurement, color or finish and feature claim was searched for in that product's own data (description, spec tabs, buy-box items and options, title), and the qualitative claims were checked by hand.

### VHX-81D-PU (p1358): 1981-93 Dodge Full-size Truck and Ramchargers VHX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1981-93 | number | found on the page |
| 10 ft | number | found on the page |
| 5 inches | number | found on the page |
| black | color/finish | found on the page |
| silver | color/finish | found on the page |
| blue | color/finish | found on the page |
| red | color/finish | found on the page |
| white | color/finish | found on the page |
| limited lifetime warranty | feature | found on the page |
| warranty | feature | found on the page |
| sioux falls | feature | found on the page |
| stepper motor | feature | found on the page |
| lcd | feature | found on the page |
| led | feature | found on the page |
| special order | feature | found on the page |
| isn't included | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |

### RTX-58C-VET-X (p1275): 1958-62 Chevy Corvette RTX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1958-62 | number | found on the page |
| 10 ft | number | found on the page |
| chrome | color/finish | found on the page |
| stepper motor | feature | found on the page |
| tft | feature | found on the page |
| led | feature | found on the page |
| special order | feature | found on the page |
| isn't included | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| rocker | feature | found on the page |

### VHX-51C (p958): 1951-52 Chevy Car VHX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1951-52 | number | found on the page |
| 10 ft | number | found on the page |
| black | color/finish | found on the page |
| silver | color/finish | found on the page |
| blue | color/finish | found on the page |
| red | color/finish | found on the page |
| white | color/finish | found on the page |
| chrome | color/finish | found on the page |
| limited lifetime warranty | feature | found on the page |
| warranty | feature | found on the page |
| sioux falls | feature | found on the page |
| stepper motor | feature | found on the page |
| led | feature | found on the page |
| special order | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| pushbutton | feature | found on the page |

### VHX-79F-MUS (p895): 1979-86 Ford Mustang VHX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1979-86 | number | found on the page |
| 10 ft | number | found on the page |
| black | color/finish | found on the page |
| silver | color/finish | found on the page |
| blue | color/finish | found on the page |
| red | color/finish | found on the page |
| carbon fiber | color/finish | found on the page |
| limited lifetime warranty | feature | found on the page |
| warranty | feature | found on the page |
| sioux falls | feature | found on the page |
| stepper motor | feature | found on the page |
| special order | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| pushbutton | feature | found on the page |

### RTX-90C-CAM-X (p1408): 1990-92 Camaro RTX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1990-92 | number | found on the page |
| 10 ft | number | found on the page |
| 5 inches | number | found on the page |
| tft | feature | found on the page |
| led | feature | found on the page |
| special order | feature | found on the page |
| isn't included | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| rocker | feature | found on the page |

### HDX-56F-PU (p1078): 1956 Ford Pickup HDX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1956 | number | found on the page |
| 10 ft | number | found on the page |
| black | color/finish | found on the page |
| silver | color/finish | found on the page |
| bluetooth | feature | found on the page |
| tft | feature | found on the page |
| special order | feature | found on the page |
| isn't included | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| touch button | feature | found on the page |

### VFD3-69M (p208): 1969-70 Ford Mustang Digital Instrument System

| Claim | Type | Source |
| --- | --- | --- |
| 1969-70 | number | found on the page |
| 0-60 | number | found on the page |
| 10 ft | number | found on the page |
| blue | color/finish | found on the page |
| teal | color/finish | found on the page |
| special order | feature | found on the page |
| isn't included | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| pushbutton | feature | found on the page |

### HDX-69C-CVL (p1059): 1969 Chevy Chevelle/ Malibu/ El Camino HDX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1969 | number | found on the page |
| black | color/finish | found on the page |
| silver | color/finish | found on the page |
| red | color/finish | found on the page |
| bluetooth | feature | found on the page |
| tft | feature | found on the page |
| special order | feature | found on the page |
| isn't included | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| touch button | feature | found on the page |

### RTX-66C-NOV-X (p1235): 1966-67 Chevy Nova RTX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1966-67 | number | found on the page |
| 10 ft | number | found on the page |
| tft | feature | found on the page |
| led | feature | found on the page |
| special order | feature | found on the page |
| isn't included | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| rocker | feature | found on the page |

### VHX-65F-PU (p1282): 1965-66 Ford Custom Cab Pickup VHX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1965-66 | number | found on the page |
| 10 ft | number | found on the page |
| 5 inches | number | found on the page |
| black | color/finish | found on the page |
| silver | color/finish | found on the page |
| blue | color/finish | found on the page |
| red | color/finish | found on the page |
| white | color/finish | found on the page |
| limited lifetime warranty | feature | found on the page |
| warranty | feature | found on the page |
| sioux falls | feature | found on the page |
| stepper motor | feature | found on the page |
| special order | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |

### VFD3-67C-IMP (p176): 1967 Chevy Caprice/Impala Digital Instrument System

| Claim | Type | Source |
| --- | --- | --- |
| 1967 | number | found on the page |
| 0-60 | number | found on the page |
| 10 ft | number | found on the page |
| 5 inches | number | found on the page |
| blue | color/finish | found on the page |
| teal | color/finish | found on the page |
| special order | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| pushbutton | feature | found on the page |

### RTX-73F-PU-X (p1253): 1973-79 Ford Pickup, 78-79 Bronco RTX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1973-79 | number | found on the page |
| 1978-79 | number | found on the page |
| 10 ft | number | found on the page |
| tft | feature | found on the page |
| led | feature | found on the page |
| special order | feature | found on the page |
| isn't included | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| rocker | feature | found on the page |

### VHX-1015 (p790): VHX-1015: Universal Five Gauge Round, Analog VHX Instrument

| Claim | Type | Source |
| --- | --- | --- |
| 59 | number | found on the page |
| 6-1/4 inches | number | found on the page |
| 3 inches | number | found on the page |
| 5-7/8 inches | number | found on the page |
| 2-3/4 inches | number | found on the page |
| 10 ft | number | found on the page |
| black | color/finish | found on the page |
| silver | color/finish | found on the page |
| blue | color/finish | found on the page |
| red | color/finish | found on the page |
| carbon fiber | color/finish | found on the page |
| limited lifetime warranty | feature | found on the page |
| warranty | feature | found on the page |
| sioux falls | feature | found on the page |
| stepper motor | feature | found on the page |
| special order | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| pushbutton | feature | found on the page |

### HDX-64F-FAL (p1181): 1964-65 Ford Falcon, Ranchero and Mustang HDX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 1964-65 | number | found on the page |
| 10 ft | number | found on the page |
| black | color/finish | found on the page |
| silver | color/finish | found on the page |
| bluetooth | feature | found on the page |
| tft | feature | found on the page |
| special order | feature | found on the page |
| isn't included | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| touch button | feature | found on the page |

### HDX-67C-CAC (p1111): 1967 Camaro with Console gauges HDX Instruments

| Claim | Type | Source |
| --- | --- | --- |
| 10 ft | number | found on the page |
| black | color/finish | found on the page |
| silver | color/finish | found on the page |
| red | color/finish | found on the page |
| bluetooth | feature | found on the page |
| tft | feature | found on the page |
| special order | feature | found on the page |
| bezel | feature | found on the page |
| metric | feature | found on the page |
| touch button | feature | found on the page |

Result: every claim in the 15 rewrites was found in that product's own page data. Hand checks included "drag racers, autocross fans and street machiners" (RTX-66C-NOV-X, description), "one-year 1956 F-series" and the visor (HDX-56F-PU, description), "late-model and diesel drivetrain swaps" (RTX-73F-PU-X, description), "the layout the '59 Chevy Impala made popular" (VHX-1015, description), "can't be split up" (HDX-67C-CAC, description), the RLC clock (RTX-58C-VET-X, buy-box versions) and Ranchero (HDX-64F-FAL, title). Nothing was removed.

## New rewrites (products that had none)

### 081026-C (p706): MCL-3006-OT and MCL-3006-R '04-'13 Baggers

File: `data/descriptions/081026-C-p706.md`

**What was wrong:** no rewrite file; original copy only 38 words

> Lost a bezel or need a new harness for your MCL-3006-OT or MCL-3006-R gauges? This page carries the replacement parts for those bagger kits.
>
> The large bezel fits the speedometer and tachometer. The small bezel fits the oil temp and pressure, fuel level and volt gauges. You can also order a dim harness, an oil temperature sender and an oil temperature harness.
>
> The page also lists a hardware pack for the MCL-3006 gauge kits. Pick the part you need from the list, and check the part number against your kit first.

### 101069-c (p592): CUP-3001 Replacement Parts

File: `data/descriptions/101069-c-p592.md`

**What was wrong:** no rewrite file; original copy only 15 words. Short on purpose: Parts list only: cup finishes, pull block, screws and bar mount sizes.

> Here are the replacement pieces for the CUP-3001 gauge cup. The cup holds a 2-1/16 inch gauge, and you can get it in chrome without hardware or in raw steel.
>
> The pull block comes with nuts, and the rear screws are sold as a set. The photos show the cup, the pull block and the rear screw.
>
> Bar mounts are listed here too, in 7/8, 1, 1-1/4 and 1-1/2 inch sizes. Each one is made for the 2-1/16 inch gauge cup.

### 101073-C (p593): HLY-5000X Replacement Parts

File: `data/descriptions/101073-C-p593.md`

**What was wrong:** no rewrite file; original copy only 33 words. Short on purpose: Parts list only: backplate, harness, lens and speed parts.

> A cracked lens or a lost backplate doesn't mean a new speedometer. These are replacement parts for the HLY-5000X and HLY-5000X-M speedometer and tachometer.
>
> You can order the chrome backplate, the 5-pin indicator harness and the MPH replacement lens on their own.
>
> The page also lists speed parts for HLY-5000 series gauges: a cable drive speed adaptor, an adaptor for 1996 and newer H-D bikes, a transmission speed sender, a rear wheel speed sender and a universal inductive speed sender.

### 101160-C (p597): CUP-3301 Replacement Parts

File: `data/descriptions/101160-C-p597.md`

**What was wrong:** no rewrite file; original copy only 15 words. Short on purpose: Parts list only: cup finishes, pull block and screw.

> Need to replace part of a CUP-3301? This page has the pieces for that 3-3/8 inch gauge cup.
>
> The cup comes in chrome or raw steel. The pull block is sold with its nuts, and the rear screw is sold on its own.
>
> The photos show the cup, the pull block and the rear screw, so you can match what you have before you order.

### 101194-C (p711): MCL-4000 Series 1-7/8 gauges

File: `data/descriptions/101194-C-p711.md`

**What was wrong:** no rewrite file; original copy only 32 words. Short on purpose: Parts list only: bezels, backplate, clamp and two harnesses.

> These replacement parts fit Dakota Digital's 1-7/8 inch MCL-4000 series gauges. That covers the speedometers, tachometer, oil pressure, oil temperature and cylinder head temp gauges.
>
> You can get the bezel in the standard style or the retro style. A backplate and a C-clamp with two thumb nuts are listed too.
>
> There are two wire harnesses. One fits the speed, tach, oil pressure and temp gauges. The other is only for the MCL-4111 cylinder head temp gauge.

### 1300 (p1247): HDX Replacement Parts

File: `data/descriptions/1300-p1247.md`

**What was wrong:** no rewrite file; exclamation point

> An optional push button lets you move the SW1 and SW2 controls off your HDX gauge face. Mount it below the dash or a panel, or take the switch out and run it through the dash for a clean look.
>
> Most HDX gauges have touch buttons in the face, so the 391184 isn't needed to run them. It works with HDX systems only.
>
> This page also lists HDX sensors and parts. The water temp sender reads 100-300 degrees F and the solid-state oil pressure sender reads 0-100 psi, each with a 10 ft harness. A small block Chevy oil pressure adaptor, a pulse generator, a replacement control box and connection harnesses are listed too.

### 1300 (p1437): GRFX Replacement Parts

File: `data/descriptions/1300-p1437.md`

**What was wrong:** no rewrite file; no description on the page

> Replacing a sensor or a control box on a GRFX system? This page has the parts.
>
> The water temp sender reads 100-300 degrees F, and the solid-state oil pressure sender reads 0-150 psi. Each comes with a 10 ft wire harness. The small block Chevy oil pressure adaptor is machined in the USA and gives the sensor more room.
>
> You'll also find a replacement GRFX control box, a 16K PPM pulse generator, a Ford and Tremec adaptor, a BIM daisy-chain cable and a 3 ft display harness for the GRFX display and GLC clock. Bushings come in several sizes, including metric thread versions with a crush washer.

### 1300 (p579): STR-A Replacement Parts

File: `data/descriptions/1300-p579.md`

**What was wrong:** no rewrite file; original copy only 52 words. Short on purpose: Parts list only: senders, bushings, speed generators and buttons.

> Replacing a sender or a trip button on an STR-A system? These are the parts it uses.
>
> The water temp sender reads 0-300 degrees F, and bushings adapt it from 1/4 inch to 3/8 or 1/2 inch NPT. Bushings may look different from the photos. You can also get the oil pressure sender, and the photo doesn't show the actual oil sender.
>
> Speed generators come in GM and Ford styles, and the photo shows the GM one. The trip and odometer reset buttons are sold here as well.

### 1300 (p580): STR-B Replacement Parts

File: `data/descriptions/1300-p580.md`

**What was wrong:** no rewrite file; original copy only 51 words. Short on purpose: Parts list only: senders, bushings, speed generators and buttons.

> This page lists the replacement parts for the STR-B system, from senders to reset buttons.
>
> The water temp sender reads 0-300 degrees F. Bushings take it from 1/4 inch to 3/8 or 1/2 inch NPT, and they may not match the photos exactly. An oil pressure sender is listed as well, though the one in the photo isn't the actual part.
>
> Pick a GM or Ford speed generator. The GM version is the one pictured. Trip and odometer reset buttons round out the list.

### 1300 (p581): STR-C Replacement Parts

File: `data/descriptions/1300-p581.md`

**What was wrong:** no rewrite file; original copy only 57 words. Short on purpose: Parts list only: senders, bushings, speed generators and buttons.

> For the STR-C system, here's every replacement part on one page.
>
> The water temp sender has a 0-300 degree F range, and bushings adapt it from 1/4 inch to 3/8 or 1/2 inch NPT. The bushings you get may differ from the photos. There's also an oil pressure sender, which isn't the one shown in the picture.
>
> Speed generators are sold in GM and Ford versions, and the GM one is pictured. The odometer trip buttons are here too. The system comes with two of them.

### 130011 (p1140): 7" GM 7/8"M-7/8"F Speedometer Cable extension

File: `data/descriptions/130011-p1140.md`

**What was wrong:** no rewrite file. Short on purpose: One-part page: cable length, ends and use.

> Is your speed sensor too close to something under the car? This 7 inch GM speedometer cable extension lets you move it.
>
> It fits between your GM transmission and the Dakota Digital SEN-01-128 or SEN-01-5 speed sensor. That sensor comes with all VFD, VHX, HDX and RTX kits.
>
> Use it when clearance is a problem. The extra length lets you relocate the sensor around most obstacles. It has 7/8 inch male and female ends.

### 130048-36 (p1245): ECD-100 and ECD-200BT Replacement Parts

File: `data/descriptions/130048-36-p1245.md`

**What was wrong:** no rewrite file; original copy only 31 words. Short on purpose: Page lists only three cable styles and their fit; nothing more to say without padding.

> Need a new speedometer cable for an ECD-100 or ECD-200BT? These 3 ft replacement cables come in three styles.
>
> The thread-on cable has a 5/8 inch nut and fits GM, Ford and Mopar. There's also a GM clip-on cable and a Ford clip-on cable.
>
> Pick the style that matches your transmission, and you're set.

### 130070 (p1254): Small Block Chevy Oil Pressure Adaptor

File: `data/descriptions/130070-p1254.md`

**What was wrong:** no rewrite file

> The small block Chevy leaves little room for an oil pressure sensor. Instead of stacking brass fittings from the hardware store, this one-piece adapter moves the sensor up and away from the intake and distributor.
>
> It's machined in the USA. A male 1/8 inch NPT thread goes into the block, and two female 1/8 inch NPT ports take the sensor you choose.
>
> The ports sit at 45 and 90 degrees, so you can work around a lot of different setups. A 1/8 inch NPT pipe plug comes with it to seal the port you don't use.

### 130071 (p1255): Ford Gen1 and Gen2 Coyote Oil Pressure Adaptor

File: `data/descriptions/130071-p1255.md`

**What was wrong:** no rewrite file; semicolon; exclamation point

> Putting a Coyote in a classic? Oil pressure isn't on the CAN/Bus for the BIM-01-2 to read, so you need the supplied 1/8 inch NPT sensor. This brass adapter gives it a place to go.
>
> It's machined in the USA. The 1/4 inch NPTF male threads fit Gen 1 and Gen 2 Coyote blocks, and female threads take the stock sensor. A 1/8 inch NPTF side port holds the Dakota Digital oil pressure sensor. You just thread it in, with no drilling or tapping.
>
> Some 2016 Gen II F-150 engines used a Gen III style pressure switch with a black connector and a 12mm male thread. The 130071 doesn't fit that version or any Gen III engine.

### 130085 (p1436): Billet LS Oil Pressure Sensor Adapter Plate

File: `data/descriptions/130085-p1436.md`

**What was wrong:** no rewrite file; original copy only 33 words. Short on purpose: Page gives only the port size, material and included hardware.

> Need a spot for an oil pressure sensor on an LS engine? This bolt-on plate adds a single 1/8 inch NPT port for one.
>
> It's machined from billet aluminum, and all the mounting hardware comes with it. A mounting manual is on the page.

### 300056 (p715): Bar Mounting Brackets for 2-1/16 Round Gauges

File: `data/descriptions/300056-p715.md`

**What was wrong:** no rewrite file; original copy only 12 words. Short on purpose: Parts list only: two screws for four bracket models.

> These are the replacement screws for the 2-1/16 inch bar mount gauge brackets. They fit the BKT-3078, BKT-3100, BKT-3125 and BKT-3150.
>
> You can order the cup screw and the clamp screw on their own.

### 300076 (p707): PGR-1000 Series

File: `data/descriptions/300076-p707.md`

**What was wrong:** no rewrite file; original copy only 9 words. Short on purpose: Parts list only: screws and four clamps.

> Lost a screw or a clamp from a PGR-1000 series gear indicator? This page has the replacement parts.
>
> A set of two screws fits the whole series. Lower clamps are sold for the PGR-1078, PGR-1100, PGR-1125 and PGR-1150, so match the clamp to your model.

### 392004 (p716): Push Button w/ boot

File: `data/descriptions/392004-p716.md`

**What was wrong:** no rewrite file; original copy only 18 words. Short on purpose: One-part page: button with boot and the gauges it fits.

> This replacement push button comes with its boot. It fits a long list of Dakota Digital motorcycle gauges.
>
> It fits MCL-3000 and MCL-3006 gauges in both the OT and R versions, plus the MCL-3200 series. It also covers the HLY-2000, HLY-3000 and HLY-5000 series.

### 393106 (p1279): MLX Touring Direct-Fit Packages

File: `data/descriptions/393106-p1279.md`

**What was wrong:** no rewrite file; original copy only 5 words. Short on purpose: Parts list only.

> These replacement parts fit the MLX-8414 touring direct-fit gauges.
>
> The list has the MLX-8414 hardware pack and the MLX-8604 hardware package. There's a 1/2 inch UNF oil temp sensor without a harness, and an oil temp harness without a sensor. A 1/2 inch UNF to 3/8 inch NPT bushing fits 2014-16 bikes. You can also get an O-ring for the oil pressure sensor and an interconnect harness. Manuals are on the page.

### 394024 (p708): HLY-3000 Series 2-1/16 Speedometer or Tachometer

File: `data/descriptions/394024-p708.md`

**What was wrong:** no rewrite file; original copy only 9 words. Short on purpose: Parts list only: harness and button.

> Need a new harness or button for a 2-1/16 inch HLY-3000 series speedometer or tachometer? Both are here.
>
> The wire harness fits the 2-1/16 inch speedometer and tachometer. The trip and odometer push button is sold on its own too.

### 394046 (p709): HLY-3000 Series 3-3/8 Speedometer/ Tachometer and Combo

File: `data/descriptions/394046-p709.md`

**What was wrong:** no rewrite file; original copy only 10 words. Short on purpose: Parts list only: two harnesses.

> Here are the replacement harnesses for Dakota Digital's 3-3/8 inch HLY-3000 series speedometers, tachometers and combo gauges.
>
> The standard wire harness is listed, plus a separate HLY-3016 harness made for Victory bikes.

### 394167 (p1318): DCC Climate Control

File: `data/descriptions/394167-p1318.md`

**What was wrong:** no rewrite file; original copy only 38 words

> These are replacement parts for Dakota Digital's DCC series climate controllers. Each item is sold on its own, so add the number you need to your cart.
>
> There are display harnesses for the DCC-2400 and 2500, the DCC-3000 and the DCC-4000. A control box harness fits the DCC-2400, 2500, 3000 and 4000. You'll also find an HLC harness, a cabin temp sensor and a DCC control module.
>
> Some parts fit only certain systems. The clip temp sensor, the 2 inch and 2.5 inch vent sensor housings and the DCC control module are for Gen IV and V systems only. The fan control module is for Gen II DCC-2200 and 2300 systems only. Wiring and setup manuals for each DCC model are on the page.

### 620001 (p1214): Speed Sensor Adaptors

File: `data/descriptions/620001-p1214.md`

**What was wrong:** no rewrite file; original copy only 23 words. Short on purpose: Parts list only: sensor, cables, adaptor and plug.

> These cables and adaptors work with Dakota Digital's 620001 two-wire speed sensor. The 8K sensor is sold here too.
>
> You can get a stubby GM cable, a flexible 6.25 inch GM cable and a stubby Ford cable. There's also a split nut adaptor for VW speedometer cables and a speed sensor plug for 1983-95 Ford Mustangs.
>
> Dakota Digital doesn't include or sell the nylon driven gears.

### 620008 (p1142): Universal Flywheel Tachometer Pickup Sensor

File: `data/descriptions/620008-p1142.md`

**What was wrong:** no rewrite file; original copy only 21 words. Short on purpose: Page gives only fit, size and thread.

> This gear-tooth sensor reads engine speed from the flywheel for a tachometer signal. It works with the Dakota Digital DSL-1 and SGI-100BT.
>
> It's 2.575 inches long and 0.47 inches across, with an M12-1 thread. A mounting manual is on the page.

### AI (p623): MCL-5000 Series Speedometer

File: `data/descriptions/AI-p623.md`

**What was wrong:** no rewrite file; exclamation point

> American Ironhorse riders finally get a Dakota Digital gauge made for their bikes. It was the company's first product built just for American Ironhorse motorcycles.
>
> Each mounting kit has a CNC-machined bracket, plated in triple chrome, plus a harness that plugs into the stock wiring. You can mount the gauge above or below the bars. Choose the oval MCL-5100 or the spiked MCL-5200 speedometer, a chrome or black finish, and the kit for your bars: T-bar or drag bar on 2002-04 bikes, or V-bar on 2004-08 bikes. Mounting hardware is chrome only.
>
> MCL-5000 gauges carry a 2 year warranty. They ship with 0 miles on the odometer, and the factory can add mileage for $20. Call Dakota Digital to set that up.

### ANT-1000 (p105): Electric Antenna -Automotive

File: `data/descriptions/ANT-1000-p105.md`

**What was wrong:** no rewrite file

> You get AM and FM reception without a rod or aerial on the outside of the car. The ANT-1000 is built to work as well as a standard rod antenna.
>
> It needs 12 VDC. Common spots are under the upholstery, inside fiberglass body panels, or along the top of the windshield or rear window. For the best signal, mount it at least 2 inches from any steel and as high in the car as you can.
>
> The antenna is 3.5 inches long and 3/4 inch thick, and it comes with a 9 ft cable. It picks up AM and FM only.

### ANT-2000 (p241): Electric Antenna -Motorcycle

File: `data/descriptions/ANT-2000-p241.md`

**What was wrong:** no rewrite file

> Hide your radio antenna inside the fairing. The ANT-2000 picks up AM and FM with no rod on the outside, and it's built to work as well as a standard rod antenna.
>
> It fits inside a plastic or fiberglass fairing and plugs straight into a standard antenna jack. It's 3.5 inches long and 3/4 inch thick, with a 3 ft cable.
>
> It won't pick up the weather band or CB radio. It doesn't work with 2014 and newer Harley-Davidson models. A wiring and setup manual and an installation article are on the page.

### BCL-1L (p1113): Single Rotor Trunk Latch

File: `data/descriptions/BCL-1L-p1113.md`

**What was wrong:** no rewrite file; original copy only 29 words. Short on purpose: Page gives only pull side, pin and size.

> This single rotor latch releases a trunk. The trunk pin is included.
>
> Pick the pull side you need. The BCL-1R is a right pull, and it's the one in the photo. The BCL-1L is a left pull. The housing is about 4 inches long, 1-1/4 inches tall and 3/4 inch wide.

### BCL-2 (p94): Dual Rotor Door Latches

File: `data/descriptions/BCL-2-p94.md`

**What was wrong:** no rewrite file; original copy only 45 words. Short on purpose: Page gives only pairs, pins, size and fastener note.

> The BCL-2 is a pair of double rotor door latches, with a right and a left pull for the driver and passenger doors. Door pins come with them.
>
> They're sold in pairs, and each one measures 4.5 by 1.85 by 0.8 inches. The drawing shows the right-hand latch. The recommended mounting fasteners aren't included.

### BD-140 (p668): Big Dog Direct Fit Speedometer

File: `data/descriptions/BD-140-p668.md`

**What was wrong:** no rewrite file; exclamation point. Short on purpose: Page gives only fit, display colors, kept parts and warranty.

> Ready for something besides the stock analog speedo on your Big Dog? This direct-fit speedometer plugs right in and keeps the stock tach ring and built-in indicator lights.
>
> It fits bikes with a handlebar-mounted gauge, the wrap-around factory tach ring and a speedometer that's 2.8 inches across the bezel, with a 2.575 inch cutout. Pick a blue or red display.
>
> It carries a 2 year limited warranty. A wiring and setup manual is on the page.

### BIM-01-2-FAST (p1104): FAST XFI Interface Module

File: `data/descriptions/BIM-01-2-FAST-p1104.md`

**What was wrong:** no rewrite file; original copy 191 words

> Running a FAST XFI system? The BIM-01-2-FAST reads its engine data and sends it to your Dakota Digital gauges.
>
> It works with the XFI ECU, XFI 2.0, EZ-EFI 2.0 and XFI Sportsman. It doesn't work with the original EZ-EFI. A supplied inline Y-adaptor harness plugs right into the FAST XFI harness. Extra readings like vehicle speed, intake temp and gear position may be available as FAST add-ons, but Dakota Digital can't promise them.
>
> It works with VHX, HDX, RTX and VFD3 systems that have a black plastic control module only. Control boxes with the 3.5mm headphone jack input need the 394194 adaptor harness. Older systems with an aluminum control module can't connect.

### BIM-01-2-J1939 (p1328): J-1939 CAN Interface

File: `data/descriptions/BIM-01-2-J1939-p1328.md`

**What was wrong:** no rewrite file; original copy 261 words; banned: allows you to

> The BIM-01-2-J1939 wires into the CAN HI and LO lines and pulls engine and transmission data from the vehicle's computer for your gauges.
>
> Most vehicles provide tach, engine temp and the check engine light. Depending on the vehicle, you may also get speed, oil pressure, intake and ambient air temp, transmission temp, gear position, fuel pressure, boost, air/fuel ratio and fuel level. Dakota Digital can't promise those, since they depend on the ECM and its sensors.
>
> It's for J1939 CAN only. Listed matches include Mercury Racing SBF, Cummins R2.8, BIGStuff EFI and MAST Motorsports ECUs. It works with the black plastic control modules on RTX, HDX, VHX and VFD3 systems. Boxes with the 3.5mm headphone jack input need the 394193 adaptor harness, and older aluminum control modules can't connect.

### BIM-01-2-MSD (p1106): MSD Atomic EFI TBI Interface Module

File: `data/descriptions/BIM-01-2-MSD-p1106.md`

**What was wrong:** no rewrite file; original copy 198 words

> If your engine runs an MSD Atomic TBI EFI kit, the BIM-01-2-MSD reads its data and sends it to your gauges. It's not compatible with the Atomic LS EFI.
>
> A supplied Y-adaptor harness plugs into the MSD Atomic handheld display or throttle body. Some MSD add-on data, like oil pressure, may be available. Dakota Digital can't promise the coolant temp, intake temp, fuel pressure, oil pressure or air/fuel readings, since they depend on the ECM and its sensors.
>
> It works with VHX, HDX, RTX and VFD3 systems that have a black plastic control module. Control boxes with the 3.5mm headphone jack input need the 394193 adaptor harness. Older systems with an aluminum control module can't connect.

### BIM-01-2 (p752): OBD-II/ CAN Interface

File: `data/descriptions/BIM-01-2-p752.md`

**What was wrong:** no rewrite file; original copy 280 words; banned: allows you to

> Plug into the engine's diagnostic port and send its data straight to your gauges. The BIM-01-2 reads engine and transmission data from the vehicle's computer over OBD-II.
>
> Most vehicles provide speed, tach, engine temp and the check engine light. Depending on the vehicle, it can also show intake air temp, transmission temp, ambient air temp, gear position, oil pressure and boost. Dakota Digital can't promise those extra readings, since they depend on the ECM and its sensors. GM Connect and Cruise packages don't send gear position.
>
> It works with GRFX, RTX, HDX, VHX and VFD3 systems that have a black plastic control module. Control boxes with the 3.5mm headphone jack input need the 394194 adaptor harness. Older systems with an aluminum control module can't connect. It supports J1850 VPW, J1850 PWM and ISO 15765 CAN 500k with 11 bit identifiers following SAE J1979.

### BIM-03-2 (p753): Pressure Module

File: `data/descriptions/BIM-03-2-p753.md`

**What was wrong:** no rewrite file; banned: allows you to

> Add one more pressure reading to your gauges with the BIM-03-2. It shows up inside RTX, HDX, VHX and VFD3 (rev G) systems.
>
> It's built for solid-state pressure senders, which gives it very fine resolution. Senders sold here include a 0-300 psi sender, a 0-100 psi fuel pressure sender, a 30 Hg to 80 psi vacuum and boost sender and a 0-2000 psi NOS pressure sender. It replaces the BIM-03-1.
>
> It needs a black plastic control module. Boxes with the 3.5mm headphone jack input need the 394193 adaptor harness. Earlier systems with an aluminum control module can't connect. Diesel fuel pressure can spike hard enough to shorten a sender's life, so add a snubber adaptor before the sensor.

### BIM-04-2 (p755): Temperature Module

File: `data/descriptions/BIM-04-2-p755.md`

**What was wrong:** no rewrite file; original copy 163 words; banned: allows you to

> The BIM-04-2 adds another temperature reading to your RTX, HDX, VHX or VFD3 gauges. It uses ground-isolated senders, so a weak engine ground won't cause trouble.
>
> Readings show in Fahrenheit or Celsius, whichever the cluster is set to. Ford Flathead engines get a special option that keeps the highest reading in the main display and the lowest in the information center. A universal 1/8 inch NPT sender, a bushing kit and inline sender blocks for transmission or oil cooler lines are sold here. The blocks come in 5/16 and 3/8 inch sizes, and the sender is sold separately.
>
> It needs a black plastic control module. Boxes with the 3.5mm headphone jack input need the 394193 adaptor harness. Earlier systems with an aluminum control module can't connect. It replaces the BIM-04-1.

### BIM-05-1 (p756): Voltage/ Current Module

File: `data/descriptions/BIM-05-1-p756.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only the reading mix, sender and module fit.

> With the BIM-05-1, your RTX, HDX, VHX or VFD system can show up to two extra volt readings, two current readings, or one of each. An amp current sender is sold on the same page.
>
> It works with systems that have a black plastic control module. Control boxes with the 3.5mm headphone jack input need the 394193 adaptor harness. Earlier systems with an aluminum control module can't connect.

### BIM-13-2 (p785): Wideband Air/ Fuel Module

File: `data/descriptions/BIM-13-2-p785.md`

**What was wrong:** no rewrite file; banned: allows you to

> See your wideband air/fuel reading right in your gauges. The BIM-13-2 works with almost any aftermarket wideband controller, and you can set it to show air/fuel ratio or lambda.
>
> It scales its output for nearly any controller with a 0-5V output. Common brands include Innovate Motorsports, NGK, FAST and AEM.
>
> It works with VHX, HDX, RTX and VFD3 systems that have a black plastic control module. Boxes with the 3.5mm headphone jack input need the 394193 adaptor harness. Earlier systems with an aluminum control module can't connect. It replaces the BIM-13-1.

### BIM-16-1 (p759): Clock Module

File: `data/descriptions/BIM-16-1-p759.md`

**What was wrong:** no rewrite file; banned: allows you to. Short on purpose: Page gives only fit, time formats and module note.

> Want a clock in a car that never had one? The BIM-16-1 plugs into any VFD system with a plastic control box, with no holes to cut and no extra mounting hardware.
>
> It shows 12 or 24 hour time. You don't need it with RTX, HDX or VHX systems, since those already have a clock.
>
> It works with VFD3 systems that have a black plastic control module. Boxes with the 3.5mm headphone jack input need the 394193 adaptor harness. Earlier systems with an aluminum control module can't connect.

### BIM-17-2 (p760): Compass w/ Outside Temperature Module

File: `data/descriptions/BIM-17-2-p760.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only compass points, temp reading and module fit.

> Add an 8 direction compass and an outside air temperature reading without putting another gauge in the car. The BIM-17-2 shows N, NE, E, SE, S, SW, W and NW.
>
> The senders and mounting hardware are included.
>
> It works with RTX, HDX, VHX and VFD3 systems that have a black plastic control module. Boxes with the 3.5mm headphone jack input need the 394193 adaptor harness. Earlier systems with an aluminum control module can't connect. It replaces the BIM-17-1.

### BIM-19-2 (p761): Quad Air Pressure Module

File: `data/descriptions/BIM-19-2-p761.md`

**What was wrong:** no rewrite file; banned: allows you to. Short on purpose: Page gives only the bag layouts, tank reading, sender and module fit.

> Keep an eye on your air ride from the dash. The BIM-19-2 shows 2 to 4 bag pressures, set up as four corners, left and right, or front and rear. It can show tank pressure too.
>
> A 0-300 psi pressure sender is sold on the same page.
>
> It works with RTX, HDX, VHX and VFD3 systems that have a black plastic control module. Boxes with the 3.5mm headphone jack input need the 394193 adaptor harness. Earlier systems with an aluminum control module can't connect. It replaces the BIM-19-1.

### BIM-22-3 (p1108): Tire Pressure Monitoring System (TPMS)

File: `data/descriptions/BIM-22-3-p1108.md`

**What was wrong:** no rewrite file; exclamation point

> Stop kicking tires to check them. This module shows live pressure for all four tires in the message center of your HDX, RTX or GRFX system.
>
> Wireless valve stem sensors send readings to a receiver mounted in the vehicle. The tire has to come off the rim to install them. The kit includes 4 sensors, the maximum it can use, and spares are sold separately. You can reprogram it after a tire rotation or replacement.
>
> It isn't sold as a standalone system. VFD3 and VHX systems have limited compatibility when ordered at the same time as a BIM-22-3, so talk to a Dakota Digital sales rep about those.

### BIM-EFI-1 (p1425): Bridge Module for EFI Systems

File: `data/descriptions/BIM-EFI-1-p1425.md`

**What was wrong:** no rewrite file; original copy 167 words; banned: streamline

> The BIM-EFI-1 reads data from your aftermarket fuel injection ECU and sends it to VFD3, VHX, HDX, RTX or GRFX gauges. You can skip some duplicate senders and sensors, and you may get extra readings, depending on how your ECU is set up.
>
> You also need a CAN Bus harness for your ECU, sold separately. Harnesses cover Holley HP, Dominator, Terminator, Terminator X and Sniper, early Dominator as a special order, Sniper 2, FAST XFI and EZ-EFI 2.0, MSD Atomic 1 and 2, AEM, Edelbrock Pro-Flo 4, MegaSquirt, MaxxECU, MoTeC, J1939, Haltech, Aces, FiTech and HPTuners CORE.
>
> Set it up over Bluetooth from a phone or other device, and get software updates over the air. For an OEM ECU with an OBD II port, use the BIM-01-2 instead.

### BKT-3 (p253): 2-1/16" and 1-7/8" Cup Mounting Brackets

File: `data/descriptions/BKT-3-p253.md`

**What was wrong:** no rewrite file; original copy only 42 words. Short on purpose: Page gives only fit, bar sizes and finish.

> These bar mounts hold the CUP-3001 and CUP-4001 gauge cups for 2-1/16 and 1-7/8 inch gauges.
>
> Pick your handlebar size: 7/8, 1, 1-1/4 or 1-1/2 inch. Each mount is machined aluminum with show-quality triple chrome plating.

### BKT-33 (p503): 3-3/8" Cup Mounting Brackets

File: `data/descriptions/BKT-33-p503.md`

**What was wrong:** no rewrite file; original copy only 38 words. Short on purpose: Page gives only fit, bar sizes and finish.

> These bar mounts hold a 3-3/8 inch gauge cup, the CUP-3301.
>
> Choose the one for your bars: 7/8, 1, 1-1/4 or 1-1/2 inch. They're machined aluminum, finished in show-quality triple chrome.

### BKT-50 (p248): Bar Mounts

File: `data/descriptions/BKT-50-p248.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only fit, widths and finish.

> These bar mounts fit MLX-9000 and MLX-5000 series gauges. They also work with MCV-7000, MCL-5000, HLY-5000 and HLY-6000 gauges.
>
> The 1 inch and 1-1/4 inch mounts are 2.2 inches wide, and the 1-1/2 inch mount is 2.4 inches wide. Each one is machined aluminum with show-quality triple chrome plating. A side-view photo shows one with a gauge installed.

### BKT-500 (p249): Riser Mounts

File: `data/descriptions/BKT-500-p249.md`

**What was wrong:** no rewrite file; original copy only 27 words. Short on purpose: Page gives only fit, bar sizes and finish.

> Mount your gauge on the risers with this machined aluminum back plate. It fits HLY-50xx, HLY-6000, MCL-5000, MCV-7000, MLX-5000 and MLX-9000 gauges.
>
> Pick your handlebar size: 1, 1-1/4 or 1-1/2 inch. The finish is show-quality triple chrome.

### BKT-5002 (p250): Harley Top Clamps

File: `data/descriptions/BKT-5002-p250.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only the three clamp styles, finishes and fit.

> Mount the gauge right on a Harley top clamp. There are three versions.
>
> The BKT-5002 is for pull-back risers, and it angles the gauge to match the top clamp. The BKT-5003 is for flat risers and tips the gauge 35 degrees back toward you. It's the one in the photo. The BKT-5011 fits Harley Deuce mounts and comes in chrome only.
>
> Each clamp is machined aluminum, in show-quality triple chrome or black powder coat. They work with HLY-5000X, HLY-5011 and 5027, HLY-6000, MCL and MCV gauges.

### BKT-5009 (p251): Honda VTX Top Clamp Mounts

File: `data/descriptions/BKT-5009-p251.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only fit, riser styles and finish.

> This top clamp replaces the factory top clamp on a Honda VTX running 1 inch bars. It gives you mounts both above and below the bars.
>
> The BKT-5009 fits pull-back risers, and the BKT-5014 fits straight risers. Both are machined aluminum in show-quality triple chrome. They fit HLY-50xx, HLY-6000 and MCV-7000 gauges.

### BKT-5012 (p255): Raw Steel Housings

File: `data/descriptions/BKT-5012-p255.md`

**What was wrong:** no rewrite file; original copy only 11 words. Short on purpose: Page gives only fit and the housing list.

> Want to paint or powder coat your gauge housing? These raw steel housing and backplate kits fit HLY-50xx, HLY-6000 and MCV-7xxx gauges.
>
> Housings are listed for the HLY-5000X and for the MCV-7100, 7200, 7300 and 7400.

### BKT-7020 (p252): Harley Sportster Custom Mounts

File: `data/descriptions/BKT-7020-p252.md`

**What was wrong:** no rewrite file; original copy only 26 words. Short on purpose: Page gives only fit and finish.

> This custom mount is made for the Harley Sportster. It replaces the backplate on MCV-7200 and MLX-9200 gauges.
>
> It's machined aluminum with show-quality triple chrome plating.

### BZL-3000-K (p704): MCL-3000-OT and MCL-3000-R '96-03 Baggers

File: `data/descriptions/BZL-3000-K-p704.md`

**What was wrong:** no rewrite file; original copy only 37 words. Short on purpose: Parts list only.

> These are replacement parts for the MCL-3000-OT and MCL-3000-R gauges on 1996-2003 baggers.
>
> Black bezels come as a set or one at a time, large or small, for the speedometer or tach. You can also get the oil temp sender with its harness, a speed harness, a gasket for the speed and tach, a push button with boot and nuts for the lower gauges.
>
> A 3/8 inch NPT to 1/2-20 UNF bushing comes with its O-ring. The control box and harness for the MCL-3000 and MCL-3000-R are listed too.

### CALG-33 (p96): 1933-34 Chevy Master Digital Instrument System

File: `data/descriptions/CALG-33-p96.md`

**What was wrong:** no rewrite file; original copy only 35 words

> A billet aluminum dash housing comes with this Series III system, built to fit the 1933-34 Chevy Master. Six bright vacuum fluorescent gauges read in blue or teal.
>
> Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, plus high speed and high rpm recall. A metric version is a special order.
>
> A matching glove box door is sold here, plain or with a VFD clock. There's also a universal glove box cover handle. Some aluminum glove box covers may need modification. The page suggests the BIM-01-2, DIM-1 and GSS-3000 as add-ons.

### CMD-10K (p89): Ten-Function Remote Entry Systems

File: `data/descriptions/CMD-10K-p89.md`

**What was wrong:** no rewrite file; original copy only 23 words. Short on purpose: Page lists kits, warranty and relay note only.

> Control up to ten functions from your key fob with the CMD-10K remote system. It comes with a limited lifetime warranty.
>
> You can buy it alone or with actuators. Kits add two or three PDR-1 10 lb push/pull actuators, or two or three PDR-2 35 lb pulling solenoids, plus two XMT-6 six-button transmitters.
>
> Some functions may need RLY-1 or RLY-2 relay packs, depending on your setup. The wiring and setup manual is on the page.

### CMD-2000 (p91): Four-Function Remote System

File: `data/descriptions/CMD-2000-p91.md`

**What was wrong:** no rewrite file; original copy only 32 words. Short on purpose: Page gives only what it controls and what is not included.

> The CMD-2000 remote can raise and lower up to two windows. Or use it for up to two solenoids or actuators that run power door locks or release latches.
>
> Power windows, actuators and solenoids aren't included.

### CMD-4000 (p92): Four-Function Remote Entry Kits

File: `data/descriptions/CMD-4000-p92.md`

**What was wrong:** no rewrite file; original copy only 29 words. Short on purpose: Page gives only the lockout feature and actuator options.

> The CMD-4000 remote entry kits include Ignition Safety Lockout. It stops the doors from opening while the key is on.
>
> Buy the remote by itself, or add two or three 10 lb actuators, or two or three 35 lb solenoids.

### CMD-X (p90): 6-12 Function Remote Accessory Controller

File: `data/descriptions/CMD-X-p90.md`

**What was wrong:** no rewrite file; exclamation point. Short on purpose: Page gives only outputs, uses, remotes, relays and warranty.

> Power windows, door locks, a power trunk, a tonneau cover, a tilt front end or a moonroof can all run from one remote. The CMD-X gives you up to 12 fully programmable output channels.
>
> Two 6-button remote transmitters come with it, and code-hopping technology adds security. Several external relays are included, so it's ready for nearly any setup.
>
> It's backed by a limited lifetime warranty.

### CUP-3001 (p254): 2-1/16" Gauge Cups

File: `data/descriptions/CUP-3001-p254.md`

**What was wrong:** no rewrite file; original copy only 35 words. Short on purpose: Page gives only the two cup versions and their mounting.

> Mount a 2-1/16 inch gauge on your bars with one of these cups.
>
> The CUP-3001 is chrome-plated aluminum and bolts to Dakota Digital BKT-3000 series brackets. The CUP-3003 is raw machined steel, made to be welded to custom handlebars. A mounting manual with dimensions is on the page.

### CUP-3301 (p502): 3-3/8" Performance Gauge Cups

File: `data/descriptions/CUP-3301-p502.md`

**What was wrong:** no rewrite file; original copy only 24 words. Short on purpose: Page gives only use and two finishes.

> Need a big gauge you can see easily? These 3-3/8 inch cups mount any of Dakota Digital's 3-3/8 inch gauges to your bars, or anywhere else you want one.
>
> They come in chrome or raw steel.

### CUP-4001 (p545): 1-7/8" Mounting Cup

File: `data/descriptions/CUP-4001-p545.md`

**What was wrong:** no rewrite file; original copy only 29 words. Short on purpose: Page gives only fit, two finishes and gauge note.

> Any 1-7/8 inch Dakota Digital gauge mounts securely in this cup.
>
> The CUP-4001 is machined aluminum with triple chrome plating, and the CUP-4003 is raw steel. The photo shows it with a gauge, but the gauge isn't included.

### DCC-2200 (p475): DCC-2200: Digital Climate Control for Vintage Air Gen II

File: `data/descriptions/DCC-2200-p475.md`

**What was wrong:** no rewrite file; exclamation point. Short on purpose: Page gives only fit, display, finish, warranty and compatibility.

> Full climate control comes to Vintage Air Gen II A/C systems with the DCC-2200. It plugs straight into the Gen II wiring harness, and you add three temperature senders.
>
> The full-character vacuum fluorescent readout comes in blue or teal, with a brushed satin or chrome bezel. It's made in America.
>
> It has a limited 24-month warranty against manufacturer defects. It only works with Vintage Air Gen II systems, not factory equipment or other aftermarket brands. The wiring and setup manual and the dimensions are on the page.

### DCC-2500 (p821): DCC-2500: Digital Climate Controller for Vintage Air Gen IV and V

File: `data/descriptions/DCC-2500-p821.md`

**What was wrong:** no rewrite file

> Set the cabin temperature you want and let the DCC-2500 hold it. It plugs right into Vintage Air Gen IV and V A/C systems, in new builds or retrofits.
>
> It takes up the same space as the Vintage Air controller. A rotary encoder on the face handles the controls. Choose horizontal or vertical, a brushed satin or chrome bezel, and blue, red or white lighting.
>
> It measures 4.2 by 1.3 inches and needs a 3.97 by 1.07 inch cutout. It works with Gen IV and V systems that use onboard ECU part number 246204. Replacement cabin temperature sensors are sold here too.

### DCC-3000H (p897): Three-Knob Digital Climate Controller for Vintage Air Gen IV and V

File: `data/descriptions/DCC-3000H-p897.md`

**What was wrong:** no rewrite file

> Three knobs and a set-it-and-forget-it cabin temperature make the DCC-3000H easy to use. It plugs right into Vintage Air Gen IV and Gen V A/C systems, new or retrofit.
>
> It fits the same footprint as the Vintage Air controller and is made to read well day or night. Choose a brushed or chrome bezel, black or silver alloy faces, and blue, red or white lighting.
>
> Overall it's 4.2 by 1.3 inches, with a 3.97 by 1.07 inch cutout. It works with Gen IV and V systems using onboard ECU part number 246204.

### DCC-4000 (p1211): DCC-4000: HDX/RTX Style Climate Controls Air Gen-IV and V

File: `data/descriptions/DCC-4000-p1211.md`

**What was wrong:** no rewrite file; exclamation point

> Give your Vintage Air Gen IV or Gen V system automatic temperature control and a late-model feel. The DCC-4000 plugs right in.
>
> Its full-color TFT display can sit horizontal or vertical, and you pick the lighting colors. Hook it to a Dakota Digital HDX or RTX system, and its colors and brightness sync with the gauges. Choose a chrome or black bezel and black or silver alloy styling.
>
> It's 4.285 by 1.85 inches overall, with a 4.050 by 1.620 inch cutout. The needed sensors and hardware are included. It works with Gen IV and Gen V systems using onboard ECU part number 246204.

### DGS-1 (p64): Alpha-Numeric L.E.D. Gear Indicator

File: `data/descriptions/DGS-1-p64.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only colors, fit, dimming and size.

> This LED gear indicator shows shift positions for standard automatic and overdrive transmissions. Pick red, green or blue LEDs.
>
> It works with the GSS-3000 gear shift sending unit and dims for night driving when the GSS-3000's DIM terminal is active. It measures 1-3/8 by 1 inch.
>
> The GSS-3000 is required and sold separately.

### DGS-3 (p63): Round Gear/Misc. Indicator

File: `data/descriptions/DGS-3-p63.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only readings, size, colors, finish and sender note.

> The DGS-3 shows your automatic gear position, plus turn signals and high beam. One more indicator can be used for check engine, 4WD, cruise, security or anything else you need.
>
> It needs a 1-3/8 inch cutout and measures 1-1/2 inches overall. The display comes in red, blue or green, with a brushed aluminum or chrome front. The brushed version is shown.
>
> The GSS-3000 sender is required for gear position and is sold separately. A wiring manual is on the page.

### DGS-4 (p62): Oval Gear/Misc Indicators

File: `data/descriptions/DGS-4-p62.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only readings, size, colors, finish and sender note.

> Oval and compact, the DGS-4 shows your automatic gear position along with turn signals and high beam. A spare indicator can be used for check engine, 4WD, cruise, security or anything else.
>
> It needs a cutout 1-1/16 inches tall by 2-5/16 inches wide. Pick a red, blue or green display and a brushed aluminum or chrome front. Brushed is shown.
>
> You'll need the GSS-3000 sender, sold separately, to show gear position. The wiring manual is on the page.

### DGS (p482): LED Gear Position Indicator

File: `data/descriptions/DGS-p482.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only mounting, size, material and options.

> This 12 VDC LED gear indicator mounts on the dash surface. Drill holes for the LEDs, run the wires into the dash, and the LEDs hold the plate in place.
>
> The plate is 1 by 3 inches and 1/16 inch thick. It's acrylic with a textured silver face that looks like brushed aluminum, at a lower cost. Pick horizontal or vertical, with or without overdrive.
>
> The GSS-3000 is required to run it and is sold separately.

### DIM-1 (p404): Light Dimming Kit

File: `data/descriptions/DIM-1-p404.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only use, fit and hole size.

> Turn your Dakota Digital gauges down for night driving. This aluminum knob and bezel controls the dimming that's built into the instrument system.
>
> Stock dimmer switches won't work with Dakota Digital instruments, and the DIM-1 won't dim other clusters. It works with VFD3/RET, VHX, HDX and RTX systems. It doesn't work with the STR series control box or with Odyssey or Solarix gauges.
>
> You'll need a 3/8 inch hole to mount it.

### DP-1 (p87): Door Popper

File: `data/descriptions/DP-1-p87.md`

**What was wrong:** no rewrite file; original copy only 15 words. Short on purpose: Page gives only size, stroke, force and pairs.

> These door poppers push a door open for you. They're sold in pairs.
>
> Each one has a 1-3/4 inch body, 5/16 inch of stroke and 25 lbs of pushing force.

### DP-3 (p395): Super Door Popper

File: `data/descriptions/DP-3-p395.md`

**What was wrong:** no rewrite file; original copy only 17 words; exclamation point. Short on purpose: Page gives only stroke, length and force.

> The Super Door Popper gives you 1-1/2 inches of stroke.
>
> It measures 3-9/16 inches pushed in and 5-1/16 inches extended, with 25 lbs of pushing force.

### ECD-200BT (p886): ECD-200BT: Electronic Signal to Mechanical Cable Drive Adaptor

File: `data/descriptions/ECD-200BT-p886.md`

**What was wrong:** no rewrite file; original copy 176 words; exclamation point

> Keep your cable-driven speedometer with a modern electronic transmission. The ECD-200BT turns an electronic speed signal into cable drive.
>
> The case measures 5-1/2 by 3-1/2 by 2 inches. The motor is quiet enough for inside the cabin, and the waterproof case can also go under the hood or in a fenderwell. A 36 inch cable comes in GM thread-on, GM clip-on or Ford clip-on styles.
>
> Set it up with the supplied switch and LED readout, or over Bluetooth with the iOS or Android app. On OBD II vehicles, the supplied pigtail plugs into the diagnostic connector. PID control drives the cable smoothly and keeps it from overdriving the speedometer needle.

### GPS-50-2 (p837): GPS Speed/ Compass Sender/ BIM

File: `data/descriptions/GPS-50-2-p837.md`

**What was wrong:** no rewrite file; original copy 471 words; exclamation point

> More than a speed sensor, the GPS-50-2 adds speed, compass heading, altitude and automatic clock syncing to RTX, HDX, VHX and VFD3 systems. Calibration is automatic. Add a SEN-15-1 sensor for outside air temperature.
>
> It's designed and built in the USA. Accelerometers and predictive software cover spots where GPS struggles, like tunnels, overpasses and tree cover. It updates speed 10 times a second, and the optional 600041 external antenna has a 110 inch cable for cruise control use. It can also drive other electronic speedometers at 4K, 8K or 16K PPM, up to 158 mph, and send a 54,400 or 128K PPM signal to an ECM.
>
> It measures 4-3/4 by 2-3/4 by 1 inch and has a two-year warranty. BIM features need a black plastic control module, and boxes with the headphone jack input need the 394194 harness.

### GSS-3000 (p1222): Universal Gear Shift Sending Unit

File: `data/descriptions/GSS-3000-p1222.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only fit, mounting and what it replaces.

> The GSS-3000 tells your gauges which gear you're in. It sends gear position to VFD, VHX, HDX or RTX systems and to the DGS standalone indicators, or it can work on its own.
>
> The decoder is smaller than before, with inboard terminals for an easier install. Mounting hardware fits GM TH350, TH400, 700R4 and 4L60, 4L70 and 4L80 transmissions, plus Ford C-4 and C-6. Other transmissions use the included universal bracket.
>
> It replaces the GSS-1000 and GSS-2000. Dakota Digital gear indicators are sold separately.

### Gift (p578): Gift Certificate

File: `data/descriptions/Gift-p578.md`

**What was wrong:** no rewrite file; exclamation point. Short on purpose: Page gives only the gift idea and amounts.

> Not sure which part your spouse, kid or buddy wants? A Dakota Digital gift certificate saves you from guessing.
>
> Not everyone knows a T56 from a blow torch, and that's fine. Let them pick out exactly what they had in mind.
>
> Gift certificates come in $50, $100 and $200 amounts.

### HDX-68D-CHG (p1090): 1968-70 Dodge Charger, Super Bee, Coronet R/T, 1970 Plymouth GTX and Road Runner

File: `data/descriptions/HDX-68D-CHG-p1090.md`

**What was wrong:** no rewrite file; original copy 214 words; semicolon

> The 1968-70 Dodge Charger has starred in plenty of movies and TV shows. This direct-fit HDX system is a bolt-in upgrade for Chargers with the rallye dash, plus 1968-70 Super Bee and Coronet R/T and the 1970 GTX and Road Runner.
>
> Its billet aluminum housing takes your original switches and front bezel, which isn't included. Choose black or silver alloy faces. The speedometer reads like a 120 mph gauge with a 160 mph top end. A metric version is a special order.
>
> Pick separate lighting colors for the readings, needles and message centers. Setup works through the touch buttons or a Bluetooth app on Apple or Android. Indicators stay hidden until they light, each gauge gets its own red warning light you can set, and a central control box hooks up the included solid-state senders.

### HDX-69C-NOV (p1073): 1969-76 Chevy Nova, 73-75 Buick Apollo, 75-76 Skylark, 73-76 Olds Omega, 71-76 Pontiac Ventura

File: `data/descriptions/HDX-69C-NOV-p1073.md`

**What was wrong:** no rewrite file; original copy 172 words; semicolon; exclamation point

> Chevrolet's X-body is a favorite, and this HDX system fills its stock instrument bezel with six analog gauges and a large TFT message center. It fits 1969-76 Novas, 1973-75 Buick Apollos, 1975-76 Skylarks, 1973-76 Olds Omegas and 1971-76 Pontiac Venturas.
>
> It uses your OEM or reproduction bezel, which isn't included. Choose black or silver alloy faces. A metric version is a special order.
>
> Pick separate lighting colors for the readings, needles and message centers. Setup works through the touch buttons or a Bluetooth app on Apple or Android. Indicators stay hidden until they light, each gauge gets its own red warning light you can set, and a central control box hooks up the included solid-state senders.

### HDX-70D-CLG (p1167): 1970-74 Dodge Challenger and 1970-74 Plymouth Cuda with Rallye dash

File: `data/descriptions/HDX-70D-CLG-p1167.md`

**What was wrong:** no rewrite file; original copy 191 words; semicolon; exclamation point

> A 426 or a late-model 6.4L, this bolt-in HDX upgrade works with either in a 1970-74 Challenger or 'Cuda with the rallye dash. Six analog gauges and a clock sit beside two large full-color TFT message centers.
>
> Use your stock front bezel, which isn't included. Turn signals and brake indicators light with LEDs. Choose black or silver alloy faces. A metric version is a special order.
>
> Pick separate lighting colors for the readings, needles and message centers. Setup works through the touch buttons or a Bluetooth app on Apple or Android. Indicators stay hidden until they light, each gauge gets its own red warning light you can set, and a central control box hooks up the included solid-state senders.

### HDX-73F-PU (p1091): 1973-79 Ford Pickup, 78-79 Bronco

File: `data/descriptions/HDX-73F-PU-p1091.md`

**What was wrong:** no rewrite file; original copy 199 words; semicolon

> Ford turned the bump into a recess in 1973, and the "dentside" pickup was born. Its triple-square gauges have always been hard to update, but this direct-fit HDX system brings modern tech to 1973-79 pickups and 1978-79 Broncos.
>
> The supplied sensors and optional expansion modules let it work with the drivetrain you choose, and a full-color TFT message center shows extra info. It uses your OEM or reproduction bezel, which isn't included. It doesn't fit the E-Van. Choose black or silver alloy faces. A metric version is a special order.
>
> Pick separate lighting colors for the readings, needles and message centers. Setup works through the touch buttons or a Bluetooth app on Apple or Android. Indicators stay hidden until they light, each gauge gets its own red warning light you can set, and a central control box hooks up the included solid-state senders.

### HLC-2162 (p1202): 2-1/16" Round Universal HDX Clock

File: `data/descriptions/HLC-2162-p1202.md`

**What was wrong:** no rewrite file. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> Add a clock that matches your HDX gauges. This universal clock mounts in a 2-1/16 inch hole and comes with black or silver alloy faces.
>
> Its bezel shape and 2-5/16 inch overall diameter make it a perfect partner for the HDX-2024 package.
>
> It has to connect to an HDX control box. It can't work as a standalone clock. Wiring and mounting manuals are on the page.

### HLY-301 (p260): Round Mini Speedometer

File: `data/descriptions/HLY-301-p260.md`

**What was wrong:** no rewrite file; original copy only 57 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> The HLY-301 is an electronic mini speedometer in a 2-1/16 inch round case. Order it in MPH or KPH.
>
> It has a limited two year warranty. It ships with 0 miles on the odometer. The factory can add mileage for $20, so call Dakota Digital to set that up. The wiring manual and dimensions are on the page.

### HLY-3011 (p262): Round Performance Speedometer with Indicators

File: `data/descriptions/HLY-3011-p262.md`

**What was wrong:** no rewrite file; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> This 3-3/8 inch round performance speedometer has built-in indicators. It reads in MPH or KPH.
>
> It isn't compatible with CAN bus motorcycles. It has a limited two year warranty. It ships with 0 miles on the odometer. The factory can add mileage for $20, so call Dakota Digital to set that up.

### HLY-3016 (p264): Round Performance Speed/Tach with Indicators

File: `data/descriptions/HLY-3016-p264.md`

**What was wrong:** no rewrite file; exclamation point. Short on purpose: Page gives only the readings, compatibility, warranty and odometer note.

> Speed, tach, odometer and indicators all fit in one 3-3/8 inch round gauge. The HLY-3016 has a speedometer that reads to 199 mph and a quick bar-graph tachometer.
>
> The odometer has two trip meters you can reset, and a full set of indicators rounds it out.
>
> It isn't compatible with CAN bus motorcycles and has a limited two year warranty. It ships with 0 miles on the odometer. The factory can add mileage for $20, so call Dakota Digital to set that up.

### HLY-3021 (p263): Round Performance Tachometer

File: `data/descriptions/HLY-3021-p263.md`

**What was wrong:** no rewrite file; original copy only 19 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> The HLY-3021 is a 3-3/8 inch round performance tachometer.
>
> It isn't compatible with CAN bus motorcycles. It has a limited two year warranty, and the wiring manual and dimensions are on the page.

### HLY-3027 (p261): Round Mini Tachometer

File: `data/descriptions/HLY-3027-p261.md`

**What was wrong:** no rewrite file; original copy only 12 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> The HLY-3027 is a digital tachometer in a 2-1/16 inch round case.
>
> It has a limited two year warranty. The wiring and setup manual and the dimensions are on the page.

### HLY-3032 (p270): Round Oil Pressure

File: `data/descriptions/HLY-3032-p270.md`

**What was wrong:** no rewrite file; original copy only 29 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> This round gauge reads oil pressure from 0-150 psi, in 1 psi steps.
>
> A chrome front bezel and a non-glare, scratch-resistant lens sit on a machined aluminum housing. Oil pressure senders are sold here in 0-150 and 0-75 psi ranges. It has a limited two year warranty.

### HLY-3041 (p425): Round Water Temperature

File: `data/descriptions/HLY-3041-p425.md`

**What was wrong:** no rewrite file; original copy only 21 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> The HLY-3041 reads water temperature from 0-300 degrees F or 0-150 degrees C, in 1 degree steps.
>
> A temperature sensor is sold on the same page. It has a limited two year warranty.

### HLY-3051 (p280): Round Voltmeter

File: `data/descriptions/HLY-3051-p280.md`

**What was wrong:** no rewrite file; original copy only 11 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> The HLY-3051 is a 2-1/16 inch round digital voltmeter.
>
> It has a limited two year warranty. The wiring manual and dimensions are on the page.

### HLY-3061 (p282): Round Fuel Level

File: `data/descriptions/HLY-3061-p282.md`

**What was wrong:** no rewrite file; original copy only 25 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> This 2-1/16 inch round fuel gauge works with the stock Harley sender.
>
> The fuel display doesn't work with 2007 Harley V-Rod models. It has a limited two year warranty.

### HLY-3073 (p272): Round Oil Temperature

File: `data/descriptions/HLY-3073-p272.md`

**What was wrong:** no rewrite file; original copy only 23 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> The HLY-3073 reads oil temperature from 0-400 degrees F or 0-200 degrees C, in 1 degree steps.
>
> An oil temperature sender is sold here too. It has a limited two year warranty.

### HLY-3111 (p276): Round Cylinder Head Temperature

File: `data/descriptions/HLY-3111-p276.md`

**What was wrong:** no rewrite file; original copy only 15 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> The HLY-3111 is a round cylinder head temperature gauge.
>
> It needs the SEN-3111 sensor, which is sold on the same page. It has a limited two year warranty.

### HLY-3191 (p274): Round Air Pressure

File: `data/descriptions/HLY-3191-p274.md`

**What was wrong:** no rewrite file; original copy only 29 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> This round gauge reads air pressure from 0-150 psi, in 1 psi steps.
>
> It has a chrome front bezel, a non-glare, scratch-resistant lens and a machined aluminum housing. A 0-150 psi air pressure sender is sold here. It has a limited two year warranty.

### HLY-3401 (p490): Round Performance Multi-function Gauge

File: `data/descriptions/HLY-3401-p490.md`

**What was wrong:** no rewrite file; exclamation point; banned: allows you to. Short on purpose: Page gives only readings, sender notes and warranty.

> One 3-3/8 inch digital gauge shows voltage, fuel level, oil pressure and oil or water temperature, and it reads easily. The HLY-3401 is a performance quad display.
>
> Temperature reads 0-300 degrees F or 0-150 degrees C, in 1 degree steps. The temperature and oil pressure senders are included. The fuel gauge needs the stock Harley-Davidson fuel sender, which isn't included, and the fuel display doesn't work with 2007 V-Rod models.
>
> It has a limited 24-month warranty against manufacturer defects.

### HLY-3402 (p331): Round Multifunction Gauge

File: `data/descriptions/HLY-3402-p331.md`

**What was wrong:** no rewrite file; original copy only 41 words; exclamation point. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> The HLY-3402 is a 2-1/16 inch round multi-function gauge with several display options. Warning points you can adjust help you keep an eye on every reading.
>
> The fuel display doesn't work with 2007 Harley V-Rod models. It has a limited two year warranty.

### HND-8-C (p1431): VCM Series Column-Mounted Cruise Control Switch

File: `data/descriptions/HND-8-C-p1431.md`

**What was wrong:** no rewrite file; em dash

> Mount your cruise control switch right on the column. The HND-8 is made for Dakota Digital VCM series cruise control systems only. It's not for OEM or CRS systems.
>
> On GM or aftermarket columns, like ididit or Flaming River, the included flat-end attachment mounts with one screw. For other columns, trim an existing turn signal lever that's 0.29 inch across or smaller, slide the HND-8 on and lock it with hidden set screws.
>
> Pick a chrome or black center accent shaft. The black version is listed as coming soon. It has a 5-year warranty.

### IND-1A (p1246): LED lights and plate for DGS-12 and DGS-13

File: `data/descriptions/IND-1A-p1246.md`

**What was wrong:** no rewrite file. Short on purpose: Thin page: only size, fit, range, warranty and manual notes.

> These are the LED lights and plates for DGS-12, DGS-12V, DGS-13 and DGS-13V gear indicators.
>
> The 0.158 inch LEDs come in amber, green or red. Replacement plates come horizontal or vertical, with or without overdrive. Each plate is 1 by 3 inches and 1/16 inch thick, acrylic with a textured silver face that looks like brushed aluminum.

### ION-01-6 (p291): Ion Series, Speedometer/Tachometer

File: `data/descriptions/ION-01-6-p291.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only styling, options and odometer note.

> The Ion Series puts sleek, modern looks and precise digital readings into a custom build. This speedometer and tachometer sits in a fully machined aluminum housing.
>
> Choose a brushed satin or chrome bezel, blue or teal display, and MPH and Fahrenheit or km/h and Celsius. A non-glare lens is only offered with the teal display. Speed sensors for cable-driven setups are listed on the page, and the GSS-3000 is a popular add-on.
>
> It ships with 0 miles on the odometer. The factory can add mileage for $20, so call Dakota Digital to set that up.

### ION-03-1 (p324): Ion Series, Oil Pressure

File: `data/descriptions/ION-03-1-p324.md`

**What was wrong:** no rewrite file; original copy only 49 words. Short on purpose: Page gives only range, finishes and sender note.

> This Ion Series gauge shows oil pressure from 0-150 psi, in 1 psi steps. It has the series' fully machined aluminum housing and modern look.
>
> Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens is offered on teal only. A sender is required and sold separately, in 1/8 inch NPT or 10mm.

### ION-04-1 (p362): Ion Series, Water Temperature

File: `data/descriptions/ION-04-1-p362.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only range, finishes and sender list.

> Ion Series styling meets a water temperature gauge here. It reads 0-300 degrees F or 0-150 degrees C, in 1 degree steps, inside a fully machined aluminum housing.
>
> Pick a brushed satin or chrome bezel and a blue or teal display. Only teal comes with the non-glare lens option. You'll need a water temp sender, sold here in 1/8, 3/8 and 1/2 inch NPT and in 12, 14 and 16mm.

### ION-05-1 (p356): Ion Series, Voltmeter

File: `data/descriptions/ION-05-1-p356.md`

**What was wrong:** no rewrite file; original copy only 45 words. Short on purpose: Ion gauge page: range, sensor and finish options only.

> The Ion Series voltmeter reads 0-17.0 VDC in 0.1 volt steps. Its fully machined aluminum housing gives a custom build a clean, modern look.
>
> Choose a brushed satin or chrome bezel and a blue or teal display. Only the teal display offers a non-glare lens.

### ION-06-1 (p353): Ion, Fuel Level

File: `data/descriptions/ION-06-1-p353.md`

**What was wrong:** no rewrite file; original copy only 51 words. Short on purpose: Ion gauge page: range, sensor and finish options only.

> Track your fuel level from 0-99% with this Ion Series gauge. It's preset to work with many sender ranges, including GM30, GM90, GM250, Ford10, Ford150, VDO, Stewart Warner/Sun and Import.
>
> The SEN-06-1 universal sensor fits most fuel tanks and is sold here. Choose a brushed satin or chrome bezel and a blue or teal display. Only the teal display offers a non-glare lens.

### ION-14-1 (p542): Ion Series, Ambient Air Temperature

File: `data/descriptions/ION-14-1-p542.md`

**What was wrong:** no rewrite file; original copy only 49 words. Short on purpose: Ion gauge page: range, sensor and finish options only.

> This Ion Series gauge shows ambient air temperature from -40 to 250 degrees F or -40 to 120 degrees C. The housing is fully machined aluminum.
>
> It needs the SEN-15-1 sensor, sold on the same page. Choose a brushed satin or chrome bezel and a blue or teal display. Only the teal display offers a non-glare lens.

### ION-15-1 (p543): Ion Series, Amplifier Temperature

File: `data/descriptions/ION-15-1-p543.md`

**What was wrong:** no rewrite file; original copy only 49 words. Short on purpose: Ion gauge page: range, sensor and finish options only.

> Keep tabs on amplifier temperature with this Ion Series gauge. It reads -40 to 250 degrees F or -40 to 120 degrees C.
>
> The SEN-15-1 sensor is required and sold here. Choose a brushed satin or chrome bezel and a blue or teal display. Only the teal display offers a non-glare lens.

### ION-16-1-S-T (p505): Ion Series, Digital Clock

File: `data/descriptions/ION-16-1-S-T-p505.md`

**What was wrong:** no rewrite file; original copy only 38 words. Short on purpose: Ion gauge page: range, sensor and finish options only.

> Add a digital clock with Ion Series styling to your dash. It has a fully machined aluminum housing.
>
> This version has a satin brushed bezel and teal lighting. The non-glare lens option is only for teal displays.

### ION-20-1 (p544): Ion Series, Amp Current

File: `data/descriptions/ION-20-1-p544.md`

**What was wrong:** no rewrite file; original copy only 48 words. Short on purpose: Ion gauge page: range, sensor and finish options only.

> The Ion Series amp gauge reads current from 0-250 amps, in 1 amp steps, inside a fully machined aluminum housing.
>
> You'll need the SEN-20-3 sensor, which is sold on the same page. Choose a brushed satin or chrome bezel and a blue or teal display. Only the teal display offers a non-glare lens.

### ION-50-1 (p310): Ion Series, 6 Gauge Kit

File: `data/descriptions/ION-50-1-p310.md`

**What was wrong:** no rewrite file; semicolon

> Get a full set of Ion Series gauges in one kit. You get the clean look of fully machined aluminum housings and precise digital readings.
>
> The kit covers speed and tach, oil pressure, water temp, volts and fuel level, with wiring manuals for each. The oil pressure, water temp and speed senders are included. Choose a brushed satin or chrome bezel, a blue or teal display, and MPH and Fahrenheit or km/h and Celsius. The GSS-3000 is a popular add-on.
>
> Systems ship with 0 miles on the odometer. The factory can set your mileage for $20, so contact Dakota Digital to arrange it.

### KN-3 (p59): Kugel Nut

File: `data/descriptions/KN-3-p59.md`

**What was wrong:** no rewrite file; original copy only 25 words. Short on purpose: Page gives only fit and thread for two nuts.

> Kugel nuts fit Kugel and Lokar shift linkages.
>
> The KN-3 has a standard thread and works with all transmissions except the 700R4. The KN-4 has a metric thread for 700R4, 4L60 and 4L80 transmissions.

### LACT-MNT (p1196): Linear Actuator Hardware -LACT

File: `data/descriptions/LACT-MNT-p1196.md`

**What was wrong:** no rewrite file; original copy only 22 words. Short on purpose: Page lists only the two hardware kits.

> These are the hardware kits for LACT linear actuators.
>
> The LACT-MNT mounting kit has two base plates and U-brackets, two 1-1/4 inch studs and four 3/4 inch bolts. The LACT-ELEC kit has the switch and wiring harness.

### LACT (p58): Linear Actuator

File: `data/descriptions/LACT-p58.md`

**What was wrong:** no rewrite file

> Lift a trunk lid, tonneau cover, amp rack, compartment cover or storage drawer with a LACT linear actuator. It pushes and pulls with 110 lbs of force.
>
> Pick a 6, 8, 10 or 12 inch stroke. Each one has built-in limit switches and comes with machined aluminum mounting brackets, a control switch and a wiring harness. The mounting plate is 1-1/8 by 1-1/2 inches.
>
> For simpler, safer use, add a PAC-3100 controller for one actuator or a PAC-3200 for two moving together. The controllers give you three preset positions, trigger wires for remote use and a safety reverse if something blocks the travel.

### LAS-RGB (p1368): RGB Lighting Control Module

File: `data/descriptions/LAS-RGB-p1368.md`

**What was wrong:** no rewrite file; original copy 232 words; banned: allows you to

> Match your interior lighting to your gauges, or run it on its own. The BIM-RGB controls accent LED lighting, from under-dash strips to door accents, using your own LED strips or Dakota Digital's.
>
> It drives 12VDC common anode RGB LEDs on up to four outputs. Each output handles up to 32 inches of LEDs, up to 1.85 amps or 22 watts at 12VDC. It can sync to HDX, RTX and GRFX color schemes, offers 31 colors and has optional switch inputs. Program it over Bluetooth with the Dakota Digital Accessory app. A music mode flashes the lights to the beat.
>
> LAS-RGB strips are tuned to match RTX and HDX gauges. They're rated IP68 for inside or outside the vehicle and come with brackets and a pre-wired 36 inch harness. Lengths are 6, 12 and 18 inches, and they only work with the Dakota Digital RGB lighting module.

### LAT-NLF (p652): LAT-NLF

File: `data/descriptions/LAT-NLF-p652.md`

**What was wrong:** no rewrite file; original copy only 45 words. Short on purpose: Page gives only use and current rating.

> The LAT-NLF replaces the original flasher module. Use it when you install LED lighting, or as a heavy-duty flasher for factory or aftermarket incandescent bulbs.
>
> It handles up to 25 amps, so there's room for extra accessory or trailer lighting. A wiring and setup manual is on the page.

### LAT-NR100 (p533): 1967-68 Camaro SS & Standard

File: `data/descriptions/LAT-NR100-p533.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1967-68 Camaro SS and Standard. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR100 (p535): 1970-73 Camaro

File: `data/descriptions/LAT-NR100-p535.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1970-73 Camaro. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR101 (p532): 1967-68 Camaro RS

File: `data/descriptions/LAT-NR101-p532.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1967-68 Camaro RS for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR111 (p534): 1969 Camaro SS & RS

File: `data/descriptions/LAT-NR111-p534.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1969 Camaro SS and RS an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR112 (p629): 1966 GTO

File: `data/descriptions/LAT-NR112-p629.md`

**What was wrong:** no rewrite file

> Your 1966 GTO can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR120 (p527): 1962-64 Nova

File: `data/descriptions/LAT-NR120-p527.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1962-64 Nova for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR130 (p528): 1965 Nova

File: `data/descriptions/LAT-NR130-p528.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1965 Nova. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR140 (p530): 1968-69 Nova

File: `data/descriptions/LAT-NR140-p530.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1968-69 Nova. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR150 (p531): 1970-72 Nova

File: `data/descriptions/LAT-NR150-p531.md`

**What was wrong:** no rewrite file

> Your 1970-72 Nova can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR160 (p524): 1966 Chevelle

File: `data/descriptions/LAT-NR160-p524.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1966 Chevelle an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR160 (p526): 1971-72 Chevelle

File: `data/descriptions/LAT-NR160-p526.md`

**What was wrong:** no rewrite file

> Your 1971-72 Chevelle can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR160 (p529): 1966-67 Nova/ Nova Wagon

File: `data/descriptions/LAT-NR160-p529.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1966-67 Nova or Nova Wagon an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR160 (p546): 1964 Chevelle

File: `data/descriptions/LAT-NR160-p546.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1964 Chevelle for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR160 (p547): 1965 Chevelle

File: `data/descriptions/LAT-NR160-p547.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1965 Chevelle. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR160 (p631): 1966 LeMans

File: `data/descriptions/LAT-NR160-p631.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1966 LeMans. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR161 (p519): 1963 Impala

File: `data/descriptions/LAT-NR161-p519.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1963 Impala an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. The page notes that the LAT-NR161 includes a part located under the tail light assembly.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR161 (p520): 1964 Impala

File: `data/descriptions/LAT-NR161-p520.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1964 Impala. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. The page notes that the LAT-NR161 includes a part located under the tail light assembly.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR161 (p521): 1965 Impala/ Caprice

File: `data/descriptions/LAT-NR161-p521.md`

**What was wrong:** no rewrite file

> Your 1965 Impala or Caprice can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. The page notes that the LAT-NR161 includes a part located under the tail light assembly.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR161 (p522): 1967 Impala

File: `data/descriptions/LAT-NR161-p522.md`

**What was wrong:** no rewrite file; exclamation point

> Swap the bulbs in a 1967 Impala for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. The page notes that the LAT-NR161 includes a part located under the tail light assembly. It doesn't fit the Caprice of the same year.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR161 (p552): 1960 Impala/ Bel Air/ Biscayne

File: `data/descriptions/LAT-NR161-p552.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1960 Impala, Bel Air or Biscayne. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. The page notes that the LAT-NR161 includes a part located under the tail light assembly.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR161 (p553): 1961 Impala/ Bel Air/ Biscayne

File: `data/descriptions/LAT-NR161-p553.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1961 Impala, Bel Air or Biscayne an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. The page notes that the LAT-NR161 includes a part located under the tail light assembly.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR161 (p554): 1962 Impala/ Bel Air/ Biscayne

File: `data/descriptions/LAT-NR161-p554.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1962 Impala, Bel Air or Biscayne. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. The page notes that the LAT-NR161 includes a part located under the tail light assembly.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR161 (p573): 1971-73 Mustang

File: `data/descriptions/LAT-NR161-p573.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1971-73 Mustang an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. The page notes that the LAT-NR161 includes a part located under the tail light assembly.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR161 (p601): 1975-76 Caprice

File: `data/descriptions/LAT-NR161-p601.md`

**What was wrong:** no rewrite file; exclamation point

> Your 1975-76 Caprice can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. The page notes that the LAT-NR161 includes a part located under the tail light assembly. It doesn't fit the Impala of the same year.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR162 (p523): 1967 Caprice

File: `data/descriptions/LAT-NR162-p523.md`

**What was wrong:** no rewrite file; exclamation point

> LED modules light up the brake and tail lights on a 1967 Caprice. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the Impala of the same year.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR162 (p555): 1966 Impala/ Caprice

File: `data/descriptions/LAT-NR162-p555.md`

**What was wrong:** no rewrite file

> Your 1966 Impala or Caprice can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR170 (p525): 1967 Chevelle

File: `data/descriptions/LAT-NR170-p525.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1967 Chevelle. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR170 (p638): 1974-77 Camaro

File: `data/descriptions/LAT-NR170-p638.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1974-77 Camaro. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the 1977 Z28 package.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR180 (p548): 1968 Chevelle

File: `data/descriptions/LAT-NR180-p548.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1968 Chevelle an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR181 (p632): 1972 Impala/ Caprice

File: `data/descriptions/LAT-NR181-p632.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1972 Impala or Caprice an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR190 (p515): 1955 Chevrolet Car

File: `data/descriptions/LAT-NR190-p515.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1955 Chevrolet Car. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR200 (p516): 1956 Chevrolet Car

File: `data/descriptions/LAT-NR200-p516.md`

**What was wrong:** no rewrite file

> Your 1956 Chevrolet Car can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR210 (p517): 1957 Chevrolet Car

File: `data/descriptions/LAT-NR210-p517.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1957 Chevrolet Car for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR221 (p518): 1958 Chevrolet Car/ Biscayne

File: `data/descriptions/LAT-NR221-p518.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1958 Chevrolet Car or Biscayne. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR221 (p565): 1961-62 Corvette

File: `data/descriptions/LAT-NR221-p565.md`

**What was wrong:** no rewrite file

> Your 1961-62 Corvette can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR221 (p566): 1963-67 Corvette

File: `data/descriptions/LAT-NR221-p566.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1963-67 Corvette for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR230 (p536): 1967-72 Fleetside Pickup

File: `data/descriptions/LAT-NR230-p536.md`

**What was wrong:** no rewrite file

> Your 1967-72 Fleetside Pickup can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR230 (p562): 1960-66 Fleetside Pickup

File: `data/descriptions/LAT-NR230-p562.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1960-66 Fleetside Pickup. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR230 (p748): 1955-58 Cameo

File: `data/descriptions/LAT-NR230-p748.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1955-58 Cameo. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR241 (p551): 1959 Impala/ Bel Air/ Biscayne

File: `data/descriptions/LAT-NR241-p551.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1959 Impala, Bel Air or Biscayne for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the El Camino or wagon.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR251 (p556): 1968 Impala/ Caprice

File: `data/descriptions/LAT-NR251-p556.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1968 Impala or Caprice for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR261 (p557): 1969 Impala/ Caprice

File: `data/descriptions/LAT-NR261-p557.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1969 Impala or Caprice. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR270 (p577): 1970 Bel Air

File: `data/descriptions/LAT-NR270-p577.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1970 Bel Air. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR271 (p558): 1970 Impala/ Caprice

File: `data/descriptions/LAT-NR271-p558.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1970 Impala or Caprice an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR281 (p559): 1967-68 Firebird

File: `data/descriptions/LAT-NR281-p559.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1967-68 Firebird. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR291 (p560): 1969 Firebird

File: `data/descriptions/LAT-NR291-p560.md`

**What was wrong:** no rewrite file

> Your 1969 Firebird can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR310 (p549): 1969 Chevelle

File: `data/descriptions/LAT-NR310-p549.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1969 Chevelle. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR320 (p550): 1970 Chevelle

File: `data/descriptions/LAT-NR320-p550.md`

**What was wrong:** no rewrite file

> Your 1970 Chevelle can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR330 (p561): 1940-53 Pickup

File: `data/descriptions/LAT-NR330-p561.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1940-53 Pickup for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR340 (p563): 1973-87 Fleetside Pickup

File: `data/descriptions/LAT-NR340-p563.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1973-87 Fleetside Pickup an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR340 (p564): 1987-91 Suburban/ Blazer

File: `data/descriptions/LAT-NR340-p564.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1987-91 Suburban or Blazer. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR350 (p570): 1964-66 Mustang

File: `data/descriptions/LAT-NR350-p570.md`

**What was wrong:** no rewrite file

> Your 1964-66 Mustang can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR362 (p571): 1967-68 Mustang

File: `data/descriptions/LAT-NR362-p571.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1967-68 Mustang for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR370 (p567): 1966-77 Bronco

File: `data/descriptions/LAT-NR370-p567.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1966-77 Bronco. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR370 (p568): 1965-74 Econoline

File: `data/descriptions/LAT-NR370-p568.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1965-74 Econoline an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It fits models with the factory rectangular tail lights.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR370 (p569): 1964-72 Pickup

File: `data/descriptions/LAT-NR370-p569.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1964-72 Pickup. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It fits models with the factory rectangular tail lights.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR372 (p572): 1969 Mustang

File: `data/descriptions/LAT-NR372-p572.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1969 Mustang. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR380 (p614): 1973-74 Nova

File: `data/descriptions/LAT-NR380-p614.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1973-74 Nova. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR390 (p609): 1971 Bel Air

File: `data/descriptions/LAT-NR390-p609.md`

**What was wrong:** no rewrite file; exclamation point

> LED modules light up the brake and tail lights on a 1971 Bel Air. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the Impala or Caprice of the same year. For those, see the LAT-NR391.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR391 (p608): 1971 Impala/ Caprice

File: `data/descriptions/LAT-NR391-p608.md`

**What was wrong:** no rewrite file; exclamation point

> Swap the bulbs in a 1971 Impala or Caprice for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the Bel Air of the same year. For that car, see the LAT-NR390.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR401 (p610): 1977 Impala

File: `data/descriptions/LAT-NR401-p610.md`

**What was wrong:** no rewrite file; exclamation point

> Give the tail lights on your 1977 Impala an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the Caprice of the same year.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR401 (p611): 1978 Impala

File: `data/descriptions/LAT-NR401-p611.md`

**What was wrong:** no rewrite file; exclamation point

> Bright LED brake and tail lights fit right into your 1978 Impala. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the Caprice of the same year.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR402 (p612): 1980-85 Caprice

File: `data/descriptions/LAT-NR402-p612.md`

**What was wrong:** no rewrite file; exclamation point

> Your 1980-85 Caprice can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the Impala of the same year.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR402 (p613): 1986-90 Caprice

File: `data/descriptions/LAT-NR402-p613.md`

**What was wrong:** no rewrite file; exclamation point

> Swap the bulbs in a 1986-90 Caprice for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the Impala of the same year.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR402 (p630): 1983-84 Parisienne

File: `data/descriptions/LAT-NR402-p630.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1983-84 Parisienne for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR410 (p627): 1965 GTO

File: `data/descriptions/LAT-NR410-p627.md`

**What was wrong:** no rewrite file

> Give the tail lights on your 1965 GTO an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR410 (p628): 1965 Tempest

File: `data/descriptions/LAT-NR410-p628.md`

**What was wrong:** no rewrite file

> Bright LED brake and tail lights fit right into your 1965 Tempest. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR411 (p633): 1974-76 Impala

File: `data/descriptions/LAT-NR411-p633.md`

**What was wrong:** no rewrite file; exclamation point

> Bright LED brake and tail lights fit right into your 1974-76 Impala. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the 1975-76 Caprice.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR411 (p634): 1974 Caprice

File: `data/descriptions/LAT-NR411-p634.md`

**What was wrong:** no rewrite file

> Your 1974 Caprice can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR421 (p635): 1973 Impala/ Caprice

File: `data/descriptions/LAT-NR421-p635.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1973 Impala or Caprice for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It fits the layout with two red lenses and one backup light lens on each side.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR421 (p636): 1977-1979 Caprice

File: `data/descriptions/LAT-NR421-p636.md`

**What was wrong:** no rewrite file

> LED modules light up the brake and tail lights on a 1977-1979 Caprice. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR421 (p637): 1980-85 Impala

File: `data/descriptions/LAT-NR421-p637.md`

**What was wrong:** no rewrite file; exclamation point

> Give the tail lights on your 1980-85 Impala an LED upgrade. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture. It doesn't fit the Caprice of the same year.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR431 (p679): 1967 GTO

File: `data/descriptions/LAT-NR431-p679.md`

**What was wrong:** no rewrite file

> Your 1967 GTO can switch to LED brake and tail lights without new wiring. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LAT-NR442 (p705): 1970 Mustang

File: `data/descriptions/LAT-NR442-p705.md`

**What was wrong:** no rewrite file

> Swap the bulbs in a 1970 Mustang for LED brake and tail light modules. They work with the harness you have now, whether it's the original wiring or a newer replacement, and with your lens and housing.
>
> The kit has LED brake and tail modules for the left and right sides, plus the wiring and crimp connectors that resist moisture.
>
> The housing and lens aren't included, so replace them first if yours can't be cleaned up or repaired. The modules carry a limited lifetime warranty, and a wiring manual is on the page.

### LOK-1601 (p56): Braided Cable for Cruise Control Kits

File: `data/descriptions/LOK-1601-p56.md`

**What was wrong:** no rewrite file; original copy only 6 words. Short on purpose: Page gives only the two cable versions.

> These braided cables connect to a CRS cruise control. The photo shows one attached.
>
> The LOK-1601 is for carbureted engines, and the LOK-1603 is for Tuned Port Injection engines.

### MBM-09 (p1312): Boost Pressure Module

File: `data/descriptions/MBM-09-p1312.md`

**What was wrong:** no rewrite file; no description on the page. Short on purpose: Page gives only fit, range and contents.

> Add a boost reading to any MLX or MVX complete instrument system with the MBM-09 module.
>
> It reads 0-100 psi. The kit includes the MBM pressure module, a 1/8 inch barbed hose adaptor and a boost sensor with harness. A wiring and setup manual is on the page.

### MBM-17 (p1313): GPS-Powered Compass Module

File: `data/descriptions/MBM-17-p1313.md`

**What was wrong:** no rewrite file; banned: allows you to. Short on purpose: Page gives only fit, GPS note and add-on sensor.

> Get an 8 direction compass heading on any MLX or MVX instrument system. The MBM-17 uses GPS satellites instead of a magnetic compass, which can give trouble on a motorcycle.
>
> Want outside air temperature too? Add the SEN-1701 sensor, sold separately.

### MBM-19 (p1314): Air Suspension Pressure Module

File: `data/descriptions/MBM-19-p1314.md`

**What was wrong:** no rewrite file; banned: allows you to. Short on purpose: Page gives only fit and contents.

> The MBM-19 adds an air suspension pressure reading to any MLX or MVX complete instrument system.
>
> It comes with the MBM pressure module, a 5/32 inch push-in T fitting, the SEN-1901 air pressure sensor with a 1/8 inch NPT thread and harness, and cable ties. Add a second SEN-1901 for a separate front and rear reading. It's sold separately and comes with its own harness, T fitting and cable ties.

### MCH-GPS17 (p953): GPS-Powered Compass, Altimeter and Ambient Air Temp Gauge to match '96-13 HD OEM gauges

File: `data/descriptions/MCH-GPS17-p953.md`

**What was wrong:** no rewrite file; exclamation point. Short on purpose: Page gives only fit, readings, antenna note and bezels.

> Add compass, altimeter and outside air temperature readings to a 1996-2013 Harley-Davidson Touring bike. The MCH-GPS17 is made to match the stock OE gauges.
>
> Its GPS-based compass and altimeter sensor is built in, so there's no external antenna to install. Pick a chrome or black bezel. A wiring and setup manual is on the page.

### MCL-3K-B (p772): MCL Series: A La Carte and Accessory Digital Dresser Gauges

File: `data/descriptions/MCL-3K-B-p772.md`

**What was wrong:** no rewrite file

> Pick just the digital gauges you want for a 1996-2013 Harley-Davidson dresser or bagger. These are the same gauges sold in the MCL-3000-OT, MCL-3000-R, MCL-3006-OT and MCL-3006-R kits.
>
> You can also replace a single gauge and keep the rest of your factory gauges. Extra gauges cover air pressure, boost and ambient air temperature. Displays come in blue or red. With a full 6 gauge kit, you can add one more for a total of 7.
>
> Availability is limited, and the colors listed are what's left in stock. The boost gauge includes its sensor. Wiring manuals for each gauge are on the page.

### MCL-4013R (p537): 1-7/8" Mini Speedometer

File: `data/descriptions/MCL-4013R-p537.md`

**What was wrong:** no rewrite file; original copy only 8 words. Short on purpose: Page gives only size, units and colors.

> The MCL-4013 is a 1-7/8 inch mini round electronic speedometer.
>
> Order it in MPH or KPH, with a blue or red display. The wiring manual and dimensions are on the page.

### MCL-4027R (p538): 1-7/8" Mini Tachometer

File: `data/descriptions/MCL-4027R-p538.md`

**What was wrong:** no rewrite file; original copy only 13 words; exclamation point. Short on purpose: Page gives only size, colors and warranty.

> A 1-7/8 inch mini round digital tach, the MCL-4027 comes with a blue or red display.
>
> It has a limited two year warranty.

### MCL-4032R (p539): 1-7/8" Mini Oil/ Air Pressure

File: `data/descriptions/MCL-4032R-p539.md`

**What was wrong:** no rewrite file; original copy only 32 words; exclamation point. Short on purpose: Page gives only range, senders, colors and warranty.

> This 1-7/8 inch mini round gauge reads oil or air pressure, 0-150 or 0-75 psi in 1 psi steps.
>
> It needs the SEN-1031 or SEN-1032 sender, both sold here. Pick a blue or red display. It has a limited two year warranty.

### MCL-4073R (p576): 1-7/8" Mini Temperature

File: `data/descriptions/MCL-4073R-p576.md`

**What was wrong:** no rewrite file; original copy only 25 words; exclamation point. Short on purpose: Page gives only range, sender, colors and warranty.

> The MCL-4073 is a 1-7/8 inch mini round gauge for oil or water temperature. It reads 0-400 degrees F or 0-200 degrees C, in 1 degree steps.
>
> A sender is sold on the same page. Choose a blue or red display. It has a limited two year warranty.

### MCL-5100 (p598): MCL-5100

File: `data/descriptions/MCL-5100-p598.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only style, fit notes and odometer note.

> The MCL-5100 is Dakota Digital's next-generation bar mount speedometer, and it replaces the HLY-5011. Like every MCL-5000 gauge, it's easy to see in direct sun.
>
> It's an oval speedometer with a chrome or black housing. It uses BKT-50xx brackets and SEN-60xx senders, and it isn't compatible with CAN bus motorcycles.
>
> It ships with 0 miles on the odometer. The factory can add mileage for $20, so call Dakota Digital to set that up.

### MCL-5200-K (p599): MCL-5200

File: `data/descriptions/MCL-5200-K-p599.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only style, fit notes and odometer note.

> Easy to read in direct sunlight, the MCL-5200 is a spiked bar mount speedometer from the MCL-5000 series. The series replaces the HLY-5011.
>
> This one has a black housing. It works with BKT-50xx brackets and SEN-60xx senders. It won't work on CAN bus motorcycles.
>
> It ships with 0 miles on the odometer. The factory can add mileage for $20, so call Dakota Digital to set that up.

### MCL-GPS17 (p952): GPS-Powered Digital Compass and Ambient Air Temp for MCL-3000 and MCL-3006 Series gauges

File: `data/descriptions/MCL-GPS17-p952.md`

**What was wrong:** no rewrite file; semicolon; exclamation point

> Add a compass and outside air temperature to a 1996-2013 Harley-Davidson bagger running Dakota Digital MCL-3000 or MCL-3006 gauges, in OT or R form.
>
> It shows N, NE, E, SE, S, SW, W and NW, reads air temp from the factory sender and uses GPS time to keep the clock right. The GPS compass is built in, so there's no external antenna and no worry about sender placement or stereo interference. Just hook up power.
>
> Choose red or blue LED lighting to match your MCL-3000 gauges, and a chrome or black bezel.

### MCL (p653): MCL-5000 Series Speedometer

File: `data/descriptions/MCL-p653.md`

**What was wrong:** no rewrite file; exclamation point

> This MCL-5000 series speedometer mounts directly on Victory motorcycles. The VM-150 kit plugs into the stock harness in the headlight bucket and mounts in the stock spot on the upper triple tree.
>
> It fits 2002-2010 Victory bikes, except the Vision, Cross Country and Cross Roads. Choose the oval MCL-5100 or the spiked MCL-5200. The MCL-5100 is 4-1/4 by 2 inches, and the 5200 and 5400 are 4-1/2 by 2 inches. Mounting hardware is chrome only. The stock low-fuel indicator goes away with this package.
>
> It has a 2 year warranty. It ships with 0 miles on the odometer. The factory can add mileage for $20, so call Dakota Digital to set that up.

### MDX-70C-CAM (p1053): 1970-81 Camaro HDX Instruments

File: `data/descriptions/MDX-70C-CAM-p1053.md`

**What was wrong:** no rewrite file; original copy 197 words; semicolon

> GM gave the 1970-81 Camaro a European-style cockpit packed with driver-focused gauges. They looked great then, and they look tired now. This bolt-in HDX package gives you six analog needles on stepper motors and twin TFT message centers you can configure.
>
> The bezel isn't supplied, so use a stock or reproduction one. Choose black or silver alloy faces. The speedometer reads like a 120 mph gauge with a 160 mph top end. A metric version is a special order.
>
> Pick separate lighting colors for the readings, needles and message centers. Setup works through the touch buttons or a Bluetooth app on Apple or Android. Indicators stay hidden until they light, each gauge gets its own red warning light you can set, and a central control box hooks up the included solid-state senders.

### MGS-1 (p103): Magnum Shooters/ W.I.D.E. Contact

File: `data/descriptions/MGS-1-p103.md`

**What was wrong:** no rewrite file

> Get rid of the wires that cross door jambs, trunks, tailgates, trailer ramps and other moving parts. Magnum Shooters pass the current across the gap for power windows and locks, remote entry, tonneau covers, stereos, alarms and more.
>
> They're spring-loaded and adjust from 1/4 to 11/16 inch, carrying up to 60 amps of low-voltage current. Versions come with 1 to 5 contacts, and most are offered with a pin switch to run a dome light. Push-on connectors make install quick. The body is ABS plastic with machined brass contacts.
>
> They're sold in pairs, and one pair covers one door or moving part. They carry a limited lifetime warranty.

### MLX-2000 (p1161): MLX-2000 Series

File: `data/descriptions/MLX-2000-p1161.md`

**What was wrong:** no rewrite file; original copy 468 words; semicolon; exclamation point

> Replace the tank-mounted speedometer on a Road King, Softail or Dyna with a 4-1/2 to 5 inch Fat Bob dash. The MLX-2000 series fits it.
>
> Choose a black or chrome bezel, then set 31 colors for each part of the display, or use one of 12 themes. It dims at night and switches to high contrast in direct sun. The speedometer reads to 250 mph and calibrates for custom gearing. You also get a wrap-around tach, a gear indicator for 4 to 7 speeds and a voltage readout. Bluetooth works with the Android and Apple app.
>
> Versions fit 2003 and older, 2004-11, and 2011-24 bikes. Oil pressure and temp senders are sold separately. It's made in the USA with a two year warranty. It ships at 0 miles, and the installer can set the odometer during the first 100 miles.

### MLX-3000 (p1162): MLX-3000 Series

File: `data/descriptions/MLX-3000-p1162.md`

**What was wrong:** no rewrite file; original copy 318 words; semicolon; exclamation point

> The MLX-3000 series replaces the stock 3-3/8 inch tank or handlebar gauge on Sportster, Rocker and Dyna models. The MLX-3000 fits 1995-2005 carbureted Sportsters and Dynas. The MLX-3004 fits fuel-injected 2004-11 Dynas, 2004-13 Sportsters and 2008-10 Rockers. The MLX-3012 covers later Softail, Dyna, Sportster and Fat Bob models.
>
> Pick a black or chrome bezel, then choose from 31 colors and 12 themes. It dims at night and goes high contrast in direct sun. The speedometer calibrates for custom gearing and reads MPH or km/h. Bluetooth connects to the Android and Apple app.
>
> Bikes with two stock instruments, like the 2004-11 Dyna Low Rider, need a new or modified dash panel. It's made in the USA with a two year warranty. It ships with 0 miles, and the installer can set the odometer in the first 100 miles.

### MLX-5200 (p1393): MLX-5000 Series Universal Gauge

File: `data/descriptions/MLX-5200-p1393.md`

**What was wrong:** no rewrite file; original copy 211 words; exclamation point

> Everything you need fits in the small MLX-5000 handlebar gauge. Its speedometer reads to 255 MPH or km/h, with a million-mile odometer and two trip meters.
>
> Hidden indicators cover turn signals, high beam, neutral, low oil pressure and check engine. The center TFT dims for night and offers 30 lighting colors and styles. It also shows a 0-60 timer, quarter-mile time and speed and service mileage, all run by one front pushbutton.
>
> The universal wiring works with many bikes, but it isn't suggested for DATA/CAN bus models. It fits all Dakota Digital handlebar and riser brackets. Choose chrome or black, and the oval MLX-5400 at 3-1/2 by 2 inches or the spiked MLX-5200 at 4-1/2 by 2 inches.

### MLX-8414 (p1160): MLX-8414

File: `data/descriptions/MLX-8414-p1160.md`

**What was wrong:** no rewrite file; original copy 314 words; semicolon; exclamation point

> Swap the stock analog gauges on a 2014-2024 Harley-Davidson Street Glide, Road Glide, Ultra Classic, Tri-Glide or CVO touring bike for this direct plug-in digital system. It's made for bikes with a factory fairing, and add-on fairings won't work.
>
> Choose from 31 colors for each part of the display, or one of 12 themes. It dims at night and switches to high contrast in direct sun. The speedometer calibrates for custom gearing and reads MPH or km/h. The two small gauges show oil temp, fuel level and voltage, and MBM modules add boost, air pressure and compass. Bluetooth connects to the Android and Apple app. It reuses the stock chrome trim rings.
>
> It ships at 0 miles, and the installer can set the odometer in the first 100 miles. To buy, call 1-800-593-4160 or a dealer.

### MLX-8696 (p1159): MLX-8600 Series

File: `data/descriptions/MLX-8696-p1159.md`

**What was wrong:** no rewrite file; original copy 326 words; semicolon; exclamation point

> Every 1996-2013 Harley-Davidson touring model, including the Road Glide, Street Glide, Ultra Classic and CVO, can take this direct plug-in digital system. Use the MLX-8696 for 1996-2003 bikes and the MLX-8604 for 2004-2013 bikes.
>
> Start with a black or chrome bezel, then set 31 colors for each part of the display or pick one of 12 themes. It dims at night and goes high contrast in direct sun. The four small gauges show oil pressure, oil temp, fuel level and voltage, and MBM modules add boost, air pressure and compass. The speedometer calibrates for custom gearing. Bluetooth connects to the Android and Apple app.
>
> It uses the stock mounting hardware and baskets. Bikes with two small gauges use the MLX-8496 or MLX-8404, so call for details. To buy, call 1-800-593-4160 or a dealer.

### MLX-9200 (p1311): MLX-9000 Series Universal Gauge

File: `data/descriptions/MLX-9200-p1311.md`

**What was wrong:** no rewrite file; original copy 245 words; exclamation point

> These universal MLX-9000 bar-mount gauges are hardwired, so they work with stock or heavily modified bikes. Pushbuttons are built in and work with gloves on.
>
> Choose RGB lighting colors, move readouts around and pick digital or bar-graph style for several displays. The spiked MLX-9200 is 6.5 by 2 inches, and the oval MLX-9400 is 5-7/8 by 2 inches. Both come in chrome or black.
>
> Readouts include speed, tach, odometer, two trip meters, service and hour meters, volts, gear position and a clock. Oil temp and pressure need separate sensors, and fuel level needs a tank sensor. Performance readouts include high speed and rpm recall, 0-60 time and quarter-mile time and speed.

### MLX-9200 (p1338): MLX-9000 Series Universal Gauge

File: `data/descriptions/MLX-9200-p1338.md`

**What was wrong:** no rewrite file; original copy 334 words; exclamation point; banned: allows you to

> Put an MLX-9200 or MLX-9400 gauge on a 2003-2010 Victory with the VM-190 kit. It mounts to the stock upper triple tree and plugs into the stock wiring harness. It doesn't fit the Vision, Cross Country or Cross Roads.
>
> The kit has a chrome-plated bracket, all the mounting hardware and a plug-and-play harness. The gauges have built-in pushbuttons that work with gloves, RGB lighting, movable readouts and digital or bar-graph styles. The spiked MLX-9200 is 6.5 by 2 inches and the oval MLX-9400 is 5-7/8 by 2 inches, in chrome or black.
>
> Readouts include speed, tach, trip meters, gear position, volts and a clock. Oil temp and pressure need separate sensors.

### MLX-9204 (p1310): MLX-9000 Series Canbus/ Databus models

File: `data/descriptions/MLX-9204-p1310.md`

**What was wrong:** no rewrite file; original copy 293 words; exclamation point

> Pick the Databus version for most 2004-13 Harley-Davidsons, or the Canbus version for select 2014-2024 models. Either way you get the MLX-9000 bar-mount system with gloves-friendly pushbuttons, RGB lighting and movable readouts.
>
> The spiked MLX-9204 and MLX-9214 are 6.5 by 2 inches. The oval MLX-9404 and MLX-9414 are 5-7/8 by 2 inches. Chrome or black housings are offered. Readouts include speed, tach, trip meters, gear position, volts and a clock. Oil temp and pressure need separate sensors.
>
> It isn't compatible with V-Rods. Because of different OEM connectors, the MLX-9214 and MLX-9414 won't plug straight into the stock harness on 2018 and newer Breakout, Softail Standard, Street Bob and Low Rider ST models.

### MLX (p1335): MLX-9000 Series Universal Gauge

File: `data/descriptions/MLX-p1335.md`

**What was wrong:** no rewrite file; original copy 257 words; exclamation point

> The MLX-9000 series is Dakota Digital's latest bar-mount instrument system. Built-in pushbuttons work even with gloves on. The MLX-9200 and MLX-9400 universal models work with stock or highly modified bikes.
>
> Pick your RGB lighting colors, move readouts to different spots and choose digital or bar-graph style for several displays. Choose the spiked MLX-9200, 6.5 by 2 inches, or the oval MLX-9400, 5-7/8 by 2 inches, in chrome or black. Readouts include speed, tach, odometer, two trip meters, service and hour meters, volts, gear position and a clock. Oil temp and pressure need separate sensors, and fuel level needs a tank sensor.
>
> American Ironhorse brackets fit 2002-04 drag bar bikes and 2004-08 V-bar bikes. An app is offered for iOS and Android.

### MVX-2002 (p977): Harley 4 1/2" Analog Replacement Cut & Splice, 1996-2003 Models w/Tank Mounted Gauge

File: `data/descriptions/MVX-2002-p977.md`

**What was wrong:** no rewrite file; original copy 191 words; exclamation point

> Fit a 1996-2003 Road King, Softail, Deuce or Dyna that has the single 5 inch tank-mounted gauge. The MVX-2002 gives you a 140 mph speedometer and a tach with an adjustable shift point.
>
> The odometer has two trip meters you can reset, and a full set of indicators is built in. The case is 4-1/4 inches across with a 4-5/8 inch bezel. Pick a chrome or black bezel and a black or white face with gray. MBM modules add boost, air pressure or compass, and the SEN-1701 adds air temp for police bikes or bikes without it. Softails may need a Harley-Davidson oil temp adapter kit.
>
> It has a limited two year warranty. It ships with 0 miles on the odometer. You can set the mileage once, before 100 miles. If you miss that or set it wrong, the factory can fix it for $20.

### MVX-2004 (p934): Harley 4-1/2" Analog Replacement w/ Direct ECM Plug-In, 2004-2013 Models w/ Tank Mounted Gauge

File: `data/descriptions/MVX-2004-p934.md`

**What was wrong:** no rewrite file; original copy 180 words; exclamation point

> The MVX-2004 plugs into the ECM on 2004-2013 Road Kings, 2004-2010 Softails, 2007-2009 CVO Convertibles, 2004-2007 Deuces and 2004-2011 Dynas with the single 5 inch tank gauge. It doesn't fit the 2010 CVO Convertible.
>
> You get a 140 mph speedometer, a tach with an adjustable shift point, two resettable trip meters and a full set of indicators. The case is 4-1/4 inches across with a 4-5/8 inch bezel. Choose a chrome or black bezel and a black or white face with gray. MBM modules can add more readings. Softails may need a Harley-Davidson oil temp adapter kit.
>
> It has a limited two year warranty. It ships with 0 miles on the odometer. You can set the mileage once, before 100 miles. If you miss that or set it wrong, the factory can fix it for $20.

### MVX-2011 (p1002): 2011-2024 Softail, 2012-2017 Dyna and 2014-2024 Road King. Direct Plug-in for 4-1/2" tank

File: `data/descriptions/MVX-2011-p1002.md`

**What was wrong:** no rewrite file; exclamation point

> Plug the MVX-2011 into the 4-1/2 inch tank dash of a 2011-2024 Softail, 2012-2017 Dyna or 2014-2024 Road King. It doesn't fit the 2011-2012 CVO Convertible or any low profile console.
>
> It has a 140 mph speedometer, a tach with an adjustable shift point, an odometer with two resettable trip meters and a full set of indicators. The case is 4-1/4 inches across with a 4-5/8 inch bezel. Choose a chrome or black bezel and a black or white face with gray. MBM modules can add more readings.
>
> It has a limited two year warranty. It ships with 0 miles on the odometer. You can set the mileage once, before 100 miles. If you miss that or set it wrong, the factory can fix it for $20.

### MVX-8600 (p888): MVX-8K Series, Analog/Digital Plug-in Instrumentation

File: `data/descriptions/MVX-8600-p888.md`

**What was wrong:** no rewrite file; exclamation point

> Analog gauges for your touring bike that are actually exciting. The MVX series bagger gauges come with 2 bezel options, 4 backgrounds and 7 lighting colors, and you set the pointer, backlight and LCD colors on their own.
>
> The 6-gauge sets come in versions for 1996-2003 and 2004-2013 Harley baggers. The LCD message centers in the speedometer and tach can show speed, rpm, volts, fuel, oil pressure, oil temp and air temp. They also show miles to empty and 0-60 and quarter-mile speed and time.
>
> To buy this kit, call 1-800-593-4160 or contact a dealer. An installation article from American Bagger is on the page.

### ODY-01-3 (p296): Odyssey Series I, Mini Speedometer

File: `data/descriptions/ODY-01-3-p296.md`

**What was wrong:** no rewrite file. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> The Odyssey Series I mini speedometer reads in MPH or KPH. Speed sensors for cable-driven setups are listed on the page.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal. It ships with 0 miles on the odometer, and the factory can add mileage for $20.

### ODY-02-7 (p297): Odyssey Series I, Mini Tachometer

File: `data/descriptions/ODY-02-7-p297.md`

**What was wrong:** no rewrite file; original copy only 39 words. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> This Odyssey Series I mini tachometer gives you a digital rpm reading.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-03-1 (p321): Odyssey Series I, Oil Pressure

File: `data/descriptions/ODY-03-1-p321.md`

**What was wrong:** no rewrite file; original copy only 50 words. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> Oil pressure reads 0-150 psi, in 1 psi steps, on this Odyssey Series I gauge. A sender is required and sold separately, in 1/8 inch NPT or 10mm, and a metric adaptor kit is listed too.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-04-1 (p383): Odyssey Series I, Water Temperature

File: `data/descriptions/ODY-04-1-p383.md`

**What was wrong:** no rewrite file. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> The Odyssey Series I water temperature gauge reads 0-300 degrees F or 0-150 degrees C, in 1 degree steps. You'll need a water temp sender, listed on the page.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-05-1-C-T (p357): Odyssey Series I, Voltmeter

File: `data/descriptions/ODY-05-1-C-T-p357.md`

**What was wrong:** no rewrite file; original copy only 46 words. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> Volts read 0-17.0 in 0.1 volt steps on this Odyssey Series I gauge. This version has a chrome bezel and teal lighting.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. The non-glare lens is offered on teal only.

### ODY-06-1 (p380): Odyssey Series I, Fuel Level

File: `data/descriptions/ODY-06-1-p380.md`

**What was wrong:** no rewrite file; original copy only 52 words. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> Read fuel level from 0-99% with this Odyssey Series I gauge. It's preset for GM30, GM90, GM250, Ford10, Ford150, VDO, Stewart Warner/Sun and Import sender ranges, and the SEN-06-1 universal sensor fits most tanks.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-07-1 (p325): Odyssey Series I, Oil Temperature

File: `data/descriptions/ODY-07-1-p325.md`

**What was wrong:** no rewrite file; original copy only 52 words. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> This Odyssey Series I gauge reads oil temperature from 0-400 degrees F or 0-200 degrees C, in 1 degree steps. It needs the SEN-04-3 sender, sold here.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-09-5 (p377): Odyssey Series I, Vacuum/ Boost

File: `data/descriptions/ODY-09-5-p377.md`

**What was wrong:** no rewrite file; original copy only 54 words. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> Vacuum and boost read from 30 inHg to 80 psi on this Odyssey Series I gauge. Resolution is 1 inHg or 0.2 psi.
>
> The sender is now included and mounts right to the manifold, with no extra plumbing. Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-10-2 (p381): Odyssey Series I, High Resolution Fuel Pressure

File: `data/descriptions/ODY-10-2-p381.md`

**What was wrong:** no rewrite file; semicolon. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> This Odyssey Series I gauge shows high resolution fuel pressure. It requires the SEN-09-4 0-100 psi high resolution sender, sold here. Diesel pressure spikes can shorten a sender's life, so add a snubber adaptor before it.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-12-1 (p379): Odyssey Series I, Exhaust Gas Temperature

File: `data/descriptions/ODY-12-1-p379.md`

**What was wrong:** no rewrite file; original copy only 54 words. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> Exhaust gas temperature reads 150-1750 degrees F or 65-955 degrees C on this Odyssey Series I gauge, in 10 degree F or 5 degree C steps. A probe is required, with leads of 6, 10, 14 or 18 ft.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-14-1 (p316): Odyssey Series I, Ambient Air Temp

File: `data/descriptions/ODY-14-1-p316.md`

**What was wrong:** no rewrite file; original copy only 50 words. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> Outside air temperature shows on this Odyssey Series I gauge, from -40 to 250 degrees F or -40 to 120 degrees C. It needs the SEN-15-1 sensor, sold here.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-15-1-C-B (p318): Odyssey Series I, Amplifier Temp

File: `data/descriptions/ODY-15-1-C-B-p318.md`

**What was wrong:** no rewrite file; original copy only 50 words. Short on purpose: Odyssey gauge page: range, sensor, options and warranty only.

> This Odyssey Series I gauge reads amplifier temperature from -40 to 250 degrees F or -40 to 120 degrees C. It needs the SEN-15-1 sensor.
>
> Versions come with a chrome or satin brushed bezel and blue or teal lighting. Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. The non-glare lens is teal only.

### ODY-16-1 (p344): Odyssey Series I, Digital Clock

File: `data/descriptions/ODY-16-1-p344.md`

**What was wrong:** no rewrite file; original copy only 39 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Add a digital clock in the Odyssey Series I style. This one has a black bezel and a teal display.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. The non-glare lens is offered on teal displays.

### ODY-19-1 (p388): Odyssey Series I, Air Pressure

File: `data/descriptions/ODY-19-1-p388.md`

**What was wrong:** no rewrite file. Short on purpose: Gauge page: range, sensor, options and warranty only.

> This Odyssey Series I gauge reads air pressure from 0-150 psi or 0-400 psi, depending on the sender you use. Resolution is 1 psi on the 0-150 range and 2 psi on the 0-400 range.
>
> Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. Choose a brushed satin or chrome bezel and a blue or teal display. The non-glare lens comes only with teal.

### ODY-19-6 (p391): Odyssey Series I, Quad Air Pressure Monitor

File: `data/descriptions/ODY-19-6-p391.md`

**What was wrong:** no rewrite file; exclamation point

> Watch every air bag at once. The ODY-19-6 shows front and rear pressures on front/rear or four-corner air ride systems, plus air tank pressure, all on one gauge.
>
> It reads 0-300 psi in 1 psi steps. Each reading needs its own sensor, so a full four-corner system takes 4, and a fifth can watch the tank. You can order it with no senders, 3 senders or 5 senders, and extra senders are sold here too.
>
> The vacuum fluorescent display is bright and easy to see in daylight. Choose a brushed satin or chrome bezel and a blue or teal display. It has a limited 24-month warranty against manufacturer defects.

### ODY-20-1-C-B (p744): Odyssey Series I, Amp Current

File: `data/descriptions/ODY-20-1-C-B-p744.md`

**What was wrong:** no rewrite file; original copy only 46 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Read current from 0-250 amps, in 1 amp steps, on this Odyssey Series I gauge. The SEN-20-3 amp current sender is sold here.
>
> Versions come with a chrome or satin brushed bezel and blue or teal lighting. Like every Odyssey Series I gauge, its bright vacuum fluorescent display reads easily in daylight and is made to last. It has a limited 24-month warranty against manufacturer defects. The non-glare lens is teal only.

### OHC2-95C-PU (p396): Chevy Truck Overhead Console Plate

File: `data/descriptions/OHC2-95C-PU-p396.md`

**What was wrong:** no rewrite file; original copy only 59 words. Short on purpose: Thin page: little beyond the part list or one-line description.

> Put a pair of 2-1/16 inch gauges in the overhead console of a 1995-2007 Classic Chevy or GMC full-size pickup. This plate uses the spot that's normally blocked off, if your truck has it.
>
> It's billet brushed aluminum and makes a nice alternative to dash or pillar pods. Gauges aren't included.

### PAC-1300 (p42): Retained ACC Power w/ Headlight & Dome Light Control

File: `data/descriptions/PAC-1300-p42.md`

**What was wrong:** no rewrite file; original copy 207 words; exclamation point

> The PAC-1300 combines three features: automatic headlights, dome light control and retained accessory power. It turns the headlights on in low light and off once there's enough light.
>
> When you get out, it leaves the headlights on for a time you choose to light your path. The dome light also stays on for a time you set after a door closes or the key turns off.
>
> A voltage monitor shuts down the lights and accessories if voltage drops too low. That keeps enough charge in the battery to start the engine.

### PAC-2800BT (p1207): Electronic Fan Controller 70 Amp with Bluetooth Control

File: `data/descriptions/PAC-2800BT-p1207.md`

**What was wrong:** no rewrite file; original copy 289 words; exclamation point

> Run any electric cooling fan with the PAC-2800BT. It includes a 70 amp relay, and you program the fan-on and fan-off temperatures anywhere from 150-250 degrees F.
>
> It can read your existing water temp sender, or you can add a dedicated one. OBD II vehicles can get engine temp from the ECM with a BIM-01-2, sold separately. Paired with BIM-compatible Dakota Digital gauges or a BIM-01-2, it can shut the fan off at a highway speed you set. Dual or two-speed fans need a second relay, the RLY-1 or RLY-3, not included. An LED readout shows the temperature.
>
> The box is 4 by 2.25 by 1 inch and should mount in the cab or another dry spot. It has a 24-month warranty.

### PAC-3100 (p464): Single Linear Actuator Controller

File: `data/descriptions/PAC-3100-p464.md`

**What was wrong:** no rewrite file. Short on purpose: Thin page: little beyond the part list or one-line description.

> Lift a trunk lid or tonneau cover with one linear actuator and the PAC-3100. It works only with Dakota Digital 5-wire linear actuators.
>
> If something blocks the lid on the way down, it senses the extra current, stops and goes back to where it started. It also learns three heights you set, so one button takes the lid where you want it.

### PAC-3200 (p465): Dual Linear Actuator Controller

File: `data/descriptions/PAC-3200-p465.md`

**What was wrong:** no rewrite file. Short on purpose: Thin page: little beyond the part list or one-line description.

> Heavier trunk lids and tonneau covers need two motors, and the PAC-3200 runs both at once. It requires two Dakota Digital 5-wire linear actuators.
>
> It reverses and returns to its starting point if a blocked lid draws too much current on the way down. It learns three heights you choose, so one button moves the lid to each one.

### PAC-3500 (p460): Automatic Door Lock Controller

File: `data/descriptions/PAC-3500-p460.md`

**What was wrong:** no rewrite file; original copy only 40 words; banned: unlock. Short on purpose: Thin page: little beyond the part list or one-line description.

> The PAC-3500 is a door lock controller built for flexibility. Its dual relay pack works with suicide safety door pins or standard door lock actuators.

### PDR-1 (p85): 10lb. Door/Trunk Actuator

File: `data/descriptions/PDR-1-p85.md`

**What was wrong:** no rewrite file; original copy only 50 words. Short on purpose: Thin page: little beyond the part list or one-line description.

> The PDR-1 actuator pushes or pulls with up to 10 lbs of force over a full inch of travel. Use it for door latches, trunk or tonneau latches, power door locks and more.
>
> It measures 6 by 2-1/4 by 1-1/8 inches and is sold one at a time. A wiring manual is on the page.

### PDR-2 (p86): 35lb. Door/Trunk Solenoid

File: `data/descriptions/PDR-2-p86.md`

**What was wrong:** no rewrite file; original copy only 47 words. Short on purpose: Thin page: little beyond the part list or one-line description.

> Rated at 35 lbs of pulling force with 3/4 inch of travel, the PDR-2 is one of the strongest solenoids around. It can open almost any door or trunk latch.
>
> It comes with a relay and universal mounting hardware. It measures 4-1/2 inches long and 2 inches across and is sold individually.

### PGR-1 (p496): PGR-1000 Series

File: `data/descriptions/PGR-1-p496.md`

**What was wrong:** no rewrite file; original copy only 52 words; exclamation point. Short on purpose: Thin page: little beyond the part list or one-line description.

> Hook it up, ride through the gears, and the PGR-1000 programs itself. It's a universal gear indicator for nearly any bike with an electronic speed signal and a 12 volt system.
>
> It has a chrome finish and a blue display. Pick the mount for 7/8, 1, 1-1/4 or 1-1/2 inch bars, or a flush mount. Manuals and dimensions are on the page.

### RET-2000 (p226): RET-2000: 5-Hole RetroTech Digital Instrument System

File: `data/descriptions/RET-2000-p226.md`

**What was wrong:** no rewrite file; original copy only 33 words

> The RetroTech panel puts five digital gauge readouts in a 5-hole layout. It's 5-7/8 inches tall and 23-7/8 inches wide with the wings, or 12-1/4 inches wide without them.
>
> Series III displays are bright vacuum fluorescent units, easy to read and accurate, and they read in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed and high speed and rpm recall.
>
> A metric version is a special order. The BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### RET-2001-S (p227): RET-2001-S: 3-Hole RetroTech Digital Instrument Panel

File: `data/descriptions/RET-2001-S-p227.md`

**What was wrong:** no rewrite file; original copy only 25 words. Short on purpose: Thin page: little beyond the part list or one-line description.

> This 3-hole RetroTech digital panel measures 5-7/8 by 12-1/4 inches.
>
> Series III displays are bright vacuum fluorescent units, easy to read and accurate, and they read in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed and high speed and rpm recall.
>
> A metric version is a special order. Popular add-ons include the BIM-01-2, DIM-1 and GSS-3000.

### RLY-1 (p83): Single Relay with Socket 30 amp

File: `data/descriptions/RLY-1-p83.md`

**What was wrong:** no rewrite file; original copy only 9 words. Short on purpose: Thin page: little beyond the part list or one-line description.

> The RLY-1 is a single 30 amp relay pack with a socket.

### RLY-2 (p84): Dual Relay Pack

File: `data/descriptions/RLY-2-p84.md`

**What was wrong:** no rewrite file; original copy only 11 words. Short on purpose: Thin page: little beyond the part list or one-line description.

> The RLY-2 is a dual 30 amp reversing polarity relay pack with a socket.

### RLY-3 (p642): 70 Amp Relay

File: `data/descriptions/RLY-3-p642.md`

**What was wrong:** no rewrite file; original copy only 17 words. Short on purpose: Thin page: little beyond the part list or one-line description.

> This 70 amp automotive relay suits big cooling fans that pull a lot of power.

### RTX-68D-CHG-X (p1265): 1968-70 Dodge Charger, Super Bee, Coronet R/T, 1970 Plymouth GTX and Road Runner

File: `data/descriptions/RTX-68D-CHG-X-p1265.md`

**What was wrong:** no rewrite file; original copy 200 words; semicolon; exclamation point

> Mopar B-bodies with the rallye dash finally get a direct-fit RTX system that looks original. It fits the 1968-70 Charger, Super Bee and Coronet R/T, plus the 1970 GTX and Road Runner.
>
> The billet aluminum housing takes your original switches and front bezel for a true bolt-in, and the clock sits inside the tach. The needles are white when off, so you can pick any lighting color. The tach is an LED bar graph, and a TFT message center adds readings.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. One central control box keeps setup simple. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### RTX-68D-STD-X (p1291): 1968-70 Mopar B-Body: Coronet, Belvedere, Satellite and Road Runner

File: `data/descriptions/RTX-68D-STD-X-p1291.md`

**What was wrong:** no rewrite file; original copy 181 words; semicolon; exclamation point

> For 1968-70 Mopar B-bodies without the rallye dash, this stock-style RTX cluster drops right in. It fits the Coronet, Belvedere, Satellite and Road Runner and uses your stock instrument surround and dash pad.
>
> Five analog sweep gauges and a pair of TFT message centers show far more than the original did, and the key indicators are built in. The look follows the factory design until the LED backlighting comes on.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. One central control box keeps setup simple. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### RTX-69C-NOV-X (p1236): 1969-76 Chevy Nova, 73-75 Buick Apollo, 75-76 Skylark, 73-76 Olds Omega, 71-76 Pontiac Ventura

File: `data/descriptions/RTX-69C-NOV-X-p1236.md`

**What was wrong:** no rewrite file; original copy 198 words; semicolon

> The rectangular speedometer in a 1969-76 Nova and its X-body cousins leaves a lot to be desired. This RTX package fills your stock instrument bezel and fits the 1973-75 Apollo, 1975-76 Skylark, 1973-76 Omega and 1971-76 Ventura too.
>
> A full-color TFT message center hides in plain sight. LED bar graphs for oil pressure, coolant temp, fuel and volts sit under the full-sweep speedometer, and it looks right in a stock restoration.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. One central control box keeps setup simple. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### RTX-70D-CLG-X (p1266): 1970-74 Dodge Challenger and 1970-74 Cuda with Rallye dash

File: `data/descriptions/RTX-70D-CLG-X-p1266.md`

**What was wrong:** no rewrite file; original copy 183 words; semicolon; exclamation point

> 1970-74 Challengers and 'Cudas with the rallye dash get a direct-fit RTX system that bolts into the stock dash and takes your original front bezel. It's an obvious pick for a Gen III Hemi swap.
>
> Turn signals and brake indicators now light with built-in LEDs. The tach reads as an LED bar graph, and TFT message centers show extra readings. It keeps the original look until the backlighting comes on.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. One central control box keeps setup simple. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### SEN-01-1 (p109): Speedometer 8K Pulse Generator

File: `data/descriptions/SEN-01-1-p109.md`

**What was wrong:** no rewrite file; original copy 212 words

> These 8K pulse generators turn a transmission's cable drive into an electronic speed signal. The SEN-01-1 fits GM transmissions and the SEN-01-2 fits Ford or Tremec. The SEN-01-4160 is a pass-through version for GM.
>
> They're made for many adjustable aftermarket speedometers. Before using one with an OEM speedometer, contact Dakota Digital sales with your vehicle details.
>
> Have a donor GM transmission with no wiring? VSS lead harnesses for the 700, 4L60 and T56 plug into the stock speed sensor. Check your transmission's connector type before ordering. For transmissions with no cable or VSS output, the SEN-4165 magnetic pickup gives 2,000-8,000 PPM using 1 to 4 magnets, and replacement magnets are sold.

### SEN-01-1 (p620): SEN-01-1

File: `data/descriptions/SEN-01-1-p620.md`

**What was wrong:** no rewrite file. Short on purpose: Thin page: little beyond the part list or one-line description.

> These are the replacement parts for the SEN-01-1 GM speedometer cable adaptor.
>
> The SEN-01-1 is the 620001 speed generator plus the 130006 GM speed coupler. Order the 130006 and you get the center key, both coupler nuts and the O-rings. Each piece is also sold on its own.

### SEN-01-128 (p916): 128k High Frequency GM Pulse Generator

File: `data/descriptions/SEN-01-128-p916.md`

**What was wrong:** no rewrite file; exclamation point

> Swapping an early GM transmission into a car with a late-model ECM? The ECM expects 128,000 pulses per mile from the internal speed sensor. The SEN-01-128 recreates that signal from the mechanical speedometer output.
>
> It has a standard female 7/8 inch thread-on fitting and fits GM transmissions with a 7/8 inch male speedometer outlet, like the TH350, TH400, 700R4 and 200-4R. A removable, weather-tight 10 ft cable makes routing easy. Its sine wave output directly replaces the stock GM internal sensor.
>
> A 7 inch extension cable is sold for Muncie transmissions or tight spots. Ford and Tremec transmissions need the 620006 adaptor.

### SEN-01-2 (p588): Ford Speed Couplers and Cables

File: `data/descriptions/SEN-01-2-p588.md`

**What was wrong:** no rewrite file. Short on purpose: Thin page: little beyond the part list or one-line description.

> These are the replacement parts for the SEN-01-2 Ford speed sender. The complete SEN-01-2 adaptor includes every part, so you need nothing else.
>
> You can also buy single pieces: the 8K pulse generator, the Ford speed coupler, the inner cable and key, the coupler nuts for the transmission and pulse generator sides, the retaining clamp and the O-rings.

### SEN-01-4280 (p57): Pass-through Pulse Generator

File: `data/descriptions/SEN-01-4280-p57.md`

**What was wrong:** no rewrite file

> Keep your mechanical factory speedometer and add electronic cruise control, or anything else that needs an 8,000 pulse per mile square wave. The SEN-01-4280 passes the cable through and makes that signal.
>
> Its square wave resists electrical interference, and the billet aluminum body is smaller than the SEN-01-4160. The SEN-01-4220 is the same but puts out 2,000 pulses per mile. The SEN-01-4160 is a lower-cost cast metal version with an 8,000 pulse per mile sine wave, and it comes with VCM-200 kits.
>
> Every model has 5/8 and 7/8 inch male coarse-thread attachments, a 130006 adaptor for 7/8 inch speedometer gear outputs and a 10 ft wire pigtail.

### SEN-01-5 (p1248): RTX Replacement Parts

File: `data/descriptions/SEN-01-5-p1248.md`

**What was wrong:** no rewrite file; original copy only 25 words; exclamation point. Short on purpose: Thin parts or sender page: only fit, range and part list.

> Need a replacement part for an RTX system? This page has the control box, rocker switch and sensors.
>
> The 391184 rocker switch assembly can mount under the dash or a panel, or go through the dash for a clean look. You'll also find a buzzer with cable, display harnesses in 3 and 6 ft lengths, an RLC clock harness, a BIM daisy-chain cable and a 16K pulse generator. The water temp sender reads 100-300 degrees F and the solid-state oil pressure sender reads 0-100 psi, each with a 10 ft harness. A small block Chevy oil pressure adaptor, bushings in several sizes and a Ford adaptor are listed too.

### SEN-01-5 (p729): VFD3 and VFD3x Second Series Replacement Parts

File: `data/descriptions/SEN-01-5-p729.md`

**What was wrong:** no rewrite file; original copy only 36 words; exclamation point. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These replacement parts fit VFD3 and VFD3x second series systems with the plastic control box.
>
> The 391183 rocker switch assembly replaces the separate 250015 switches. Mount it under the dash or a panel, or pull the switch and run it through the dash for a clean install. The VFD3 control module, a 16K speed generator, a 3.5mm port adaptor and a sensor package are listed too. The water temp sender reads 100-300 degrees F and the solid-state oil pressure sender reads 0-100 psi, each with a 10 ft harness. A small block Chevy oil pressure adaptor, bushings in several sizes and a Ford adaptor are listed too.

### SEN-01-5 (p730): VHX Replacement Parts

File: `data/descriptions/SEN-01-5-p730.md`

**What was wrong:** no rewrite file; original copy only 46 words; exclamation point. Short on purpose: Thin parts or sender page: only fit, range and part list.

> Here are the replacement parts for VHX analog gauge systems, starting with the VHX control box.
>
> The 391183 rocker switch assembly replaces the separate 250015 switches and works only with VHX systems. Mount it under the dash, or remove the switch and run it through the dash. Cat 5 cables, BIM daisy-chain cables, an oil pressure harness, a turn signal harness and a 16K speed generator are listed. The water temp sender reads 100-300 degrees F and the solid-state oil pressure sender reads 0-100 psi, each with a 10 ft harness. A small block Chevy oil pressure adaptor, bushings in several sizes and a Ford adaptor are listed too.

### SEN-03-1 (p110): Oil Pressure Sender for individual Dakota Digital Gauges

File: `data/descriptions/SEN-03-1-p110.md`

**What was wrong:** no rewrite file. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These pressure senders are for standalone Dakota Digital gauges. The SEN-03-1 reads 0-150 psi with a dual terminal and a 1/8 inch NPT thread.
>
> The SEN-10-2 reads 0-75 psi with a single terminal, and the SEN-03-3 reads 0-150 psi with an M10 x 1 thread. The SEN-03-5 reads 0-300 psi with a dual terminal. The SEN-03-6 metric bushing kit is CNC machined from brass and comes with aluminum crush washers.
>
> Complete instrument systems with a control module use different oil pressure sensors. Look for those under Replacement Parts.

### SEN-03-1 (p124): Air Pressure Sender

File: `data/descriptions/SEN-03-1-p124.md`

**What was wrong:** no rewrite file; original copy only 59 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> Both of these universal pressure senders have a 1/8 inch NPT fitting and two posts, one for signal and one for ground.
>
> The SEN-03-1 reads 0-150 psi in 1 psi steps, and the SEN-03-5 reads 0-400 psi in 2 psi steps. They don't work with the ODY-19-6, ODYR-19-7 or SLX-19-7, which use the SEN-03-9.

### SEN-04-1 (p111): Water/Oil/Trans Temperature Sender

File: `data/descriptions/SEN-04-1-p111.md`

**What was wrong:** no rewrite file. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These temperature senders work for water, transmission or oil. They read 0-300 degrees F or 0-150 degrees C, in 1 degree steps.
>
> Fittings come in 1/8, 3/8 and 1/2 inch NPT and 12mm x 1.5. The 140022 includes 1/4, 3/8 and 1/2 inch NPT bushings. The SEN-04-5 has a 1/8 inch NPT fitting with a harness, and it's the one to use with plastic control box RTX, HDX, VHX and VFD systems or a BIM-04-2.

### SEN-04-3 (p113): Oil Temperature Sender

File: `data/descriptions/SEN-04-3-p113.md`

**What was wrong:** no rewrite file; original copy only 19 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> The SEN-04-3 oil temperature sender reads 0-400 degrees F or 0-200 degrees C, in 1 degree steps. It has a 1/8 inch NPT thread.

### SEN-04-3 (p114): Transmission Temperature Sender

File: `data/descriptions/SEN-04-3-p114.md`

**What was wrong:** no rewrite file; original copy only 33 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> Read transmission temperature with the SEN-04-3. It covers 0-400 degrees F or 0-200 degrees C in 1 degree steps and has a 1/8 inch NPT fitting.
>
> Inline sender blocks fit 5/16 or 3/8 inch transmission lines. The sender is sold separately from the blocks.

### SEN-04 (p582): STR-D/ Series II Replacement Parts

File: `data/descriptions/SEN-04-p582.md`

**What was wrong:** no rewrite file. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These replacement parts fit STR-D and Series II systems.
>
> The water temp sender reads 0-300 degrees F and comes in several thread sizes. Bushings adapt 1/8 inch NPT to 1/4, 3/8 or 1/2 inch NPT, or to 12mm or 16mm with a crush washer. The 0-100 psi oil pressure sender, GM and Ford speed generators and odometer trip buttons are listed too. The system comes with two buttons.

### SEN-04 (p583): VFD3 and VFD3x First Series Replacement Parts

File: `data/descriptions/SEN-04-p583.md`

**What was wrong:** no rewrite file. Short on purpose: Thin parts or sender page: only fit, range and part list.

> Replacing a part on a first series VFD3, VFD3X or RET system with the metal control box? Your box may look different from the photo.
>
> The water temp sender reads 0-300 degrees F, and the oil pressure sender reads 0-80 psi. GM and Ford speed generators are listed. Bushings adapt 1/8 inch NPT to 1/4, 3/8 or 1/2 inch NPT, or to 12mm or 16mm with a crush washer. Odometer trip buttons are sold too, and the system comes with two.

### SEN-06-1 (p112): Universal Fuel Level Sender

File: `data/descriptions/SEN-06-1-p112.md`

**What was wrong:** no rewrite file; original copy only 33 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> This universal fuel level sender has an adjustable float that fits many aftermarket fuel cells.
>
> Because it's universal, check your setup before you order.

### SEN-09-5 (p117): Vacuum/Boost and Fuel Pressure Sender

File: `data/descriptions/SEN-09-5-p117.md`

**What was wrong:** no rewrite file

> Two senders are on this page. The SEN-09-5 reads vacuum from -30 to 0 inHg and boost from 0-80 psi, with a 1/8 inch NPT male thread. It works only with ODY-09-5, ODYR-09-5, ODYR-25-1, SLX-09-5 and SLX-25-1 gauges.
>
> The SEN-09-4 reads 0-100 psi for boost or fuel pressure, also with a 1/8 inch NPT thread. It works only with the ODY, ODYR and SLX 09-4 and 10-2 gauges.
>
> Neither works with the BIM-03-2 pressure module, and the actual sensor may look different from the photo. On diesels, a pressure snubber or isolator may help the sensor last. This is most common on 1998-2002 Dodge Cummins trucks.

### SEN-1011 (p242): Mechanical Speedometer Cable Adaptors

File: `data/descriptions/SEN-1011-p242.md`

**What was wrong:** no rewrite file; original copy only 52 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These speed pulse generators are for cable-driven setups. Three versions are listed: the SEN-1011, the SEN-2011 and the SEN-6011.
>
> They can work on sportbikes and metric cruisers if the OEM speedometer cable is modified to a 5/8 inch thread. Some Harley-Davidson 12mm cables won't fit and may need changes or a custom cable.

### SEN-1012 (p243): Electronic Speed Sensor Adaptors and Extension

File: `data/descriptions/SEN-1012-p243.md`

**What was wrong:** no rewrite file; original copy only 53 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These adaptors connect stock 1996-2003 Harley-Davidson speed senders to Dakota Digital gauges. Each one matches a certain gauge series, so you can convert inline with no cutting or splicing.
>
> The SEN-2012 is 18 inches long. They also work on sportbikes and metric cruisers once the triangular Deutsch connector is removed.

### SEN-1017 (p244): Transmission Speed Sensors

File: `data/descriptions/SEN-1017-p244.md`

**What was wrong:** no rewrite file. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These sensors mount in the speed sensor port of most 1996-2003 OEM Harley-Davidson transmissions and aftermarket big twin transmissions, except Sportsters. They read an internal gear and send a pulse signal to your Dakota Digital speedometer.
>
> Six speed and larger transmissions need the speed sensor spacer that comes with the transmission. The sensors are machined aluminum, polished by hand.

### SEN-1018 (p245): Rear Wheel Speed Sensors

File: `data/descriptions/SEN-1018-p245.md`

**What was wrong:** no rewrite file. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These sensors mount on the rear axle spacer of most Softail and rigid bikes. They read the rear pulley bolts and send a pulse signal to the speedometer.
>
> They need a 1-3/32 inch axle spacer and measure 2 inches wide, 2-3/4 inches long and 1/2 inch thick. They won't drive a stock Harley-Davidson electronic speedometer. They're polished machined aluminum.

### SEN-1019 (p246): Universal Inductive Speed Sensors

File: `data/descriptions/SEN-1019-p246.md`

**What was wrong:** no rewrite file; original copy only 59 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These universal sensors read gear teeth, pulley bolts or any ferrous metal that passes by. They send a pulse signal to the speedometer, which shows your speed.
>
> The housing is 1/2 inch across and 1 inch long, with a 15/32 x 32 thread. They won't drive a stock Harley-Davidson electronic speedometer.

### SEN-1031 (p328): Oil and Air Pressure Senders

File: `data/descriptions/SEN-1031-p328.md`

**What was wrong:** no rewrite file; original copy only 58 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> Two oil and air pressure senders are offered, both with a 1/8 inch NPT fitting and a polished metal finish.
>
> The SEN-1031 reads 0-150 psi in 1 psi steps and has two posts, one for signal and one for ground. The SEN-1032 is a single post sender that reads 0-75 psi.

### SEN-1039 (p1018): Oil and Air Pressure Sensor

File: `data/descriptions/SEN-1039-p1018.md`

**What was wrong:** no rewrite file; original copy only 38 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> The SEN-1039 senses oil or air pressure from 0-300 psi, in 1 psi steps, with a 1/8 inch NPT fitting.
>
> It's for the MVX-2000, MVX-2004 and MVX-2011 and the MLX-2002, MLX-2004 and MLX-2011. A 1/8 to 1/4 inch bushing is included.

### SEN-1043 (p329): Oil and Water Temperature Sensor

File: `data/descriptions/SEN-1043-p329.md`

**What was wrong:** no rewrite file. Short on purpose: Thin parts or sender page: only fit, range and part list.

> The SEN-1043 oil temperature sensor screws into the crankcase, oil tank or an oil line with the right fittings. It reads 0-400 degrees F or 0-200 degrees C, has a 1/8 inch NPT thread and includes a 1/8 to 1/4 inch NPT bushing. Other spots may need drilling and tapping.
>
> The SEN-1044 reads 0-300 degrees F with a 3/8 inch NPT thread. It fits HLY-3073, MCL-3000 and MVX-2000 gauges. The SEN-1045 reads 0-400 degrees with a 1/2 inch UNF thread for 2017 and newer Harley-Davidsons.

### SEN-11-4 (p115): Cylinder Head Temperature Sender

File: `data/descriptions/SEN-11-4-p115.md`

**What was wrong:** no rewrite file; original copy only 22 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These cylinder head temperature senders come in 6, 10, 14 and 18 ft lengths.
>
> Each has a 1/2 inch ring terminal, except the SEN-11-8, an 18 ft sender made for 14mm spark plugs.

### SEN-12-4 (p116): Exhaust Gas Temperature Sender

File: `data/descriptions/SEN-12-4-p116.md`

**What was wrong:** no rewrite file; original copy only 26 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> These exhaust gas temperature senders read 0-1600 degrees F or 0-870 degrees C, in 10 degree F or 5 degree C steps.
>
> They have a 1/8 inch NPT fitting and come in 6, 10, 14 and 18 ft lengths.

### SEN-12 (p758): EGT, Head Temperature Module

File: `data/descriptions/SEN-12-p758.md`

**What was wrong:** no rewrite file. Short on purpose: Thin parts or sender page: only fit, range and part list.

> Add up to two temperature readings to your gauges with the BIM-12-2: two EGT, two CHT, or one of each. It replaces the BIM-12-1.
>
> EGT senders and cylinder head temp senders are sold here, with lead lengths from 6 to 18 ft, plus an 18 ft sender for 14mm plugs.
>
> It works with VHX, HDX, RTX and VFD3 systems that have a black plastic control module. Boxes with the 3.5mm headphone jack input need the 394193 adaptor harness. Earlier systems with an aluminum control module can't connect.

### SEN-15-1 (p120): Ambient Air Temperature Sender

File: `data/descriptions/SEN-15-1-p120.md`

**What was wrong:** no rewrite file; original copy only 6 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> The SEN-15-1 is an ambient air temperature sender.

### SEN-20-3 (p123): Amp Current Sender

File: `data/descriptions/SEN-20-3-p123.md`

**What was wrong:** no rewrite file; original copy only 11 words. Short on purpose: Thin parts or sender page: only fit, range and part list.

> The SEN-20-3 is an inductive amp current sending unit. The sensor is 0.625 inch across.

### SEN-201 (p983): DHC Ride Height Controller

File: `data/descriptions/SEN-201-p983.md`

**What was wrong:** no rewrite file; no description on the page. Short on purpose: No description on the page: only the part names.

> This page sells the ride height sensor for the DHC ride height controller, with its harness. The harness is also sold by itself, without a sensor.

### SEN-23-1 (p121): Nitrous Pressure Sender

File: `data/descriptions/SEN-23-1-p121.md`

**What was wrong:** no rewrite file; original copy only 13 words. Short on purpose: Page gives only range and thread.

> The SEN-23-1 reads nitrous pressure from 0 to 2,000 psi. It has a 1/8 inch NPT male thread.

### SEN-3111 (p330): Cylinder Head Temperature Sensor

File: `data/descriptions/SEN-3111-p330.md`

**What was wrong:** no rewrite file; no description on the page. Short on purpose: No description on the page: only the title and the HLY-3111 sensor note.

> The SEN-3111 is a cylinder head temperature sender. It's the sensor the HLY-3111 round CHT gauge requires.

### SGI-100BT (p1192): SGI-100BT: Universal Speedometer and Tachometer Interface

File: `data/descriptions/SGI-100BT-p1192.md`

**What was wrong:** no rewrite file; original copy only 41 words; exclamation point. Short on purpose: Page gives only the three functions and size.

> Three jobs fit in one 4 by 2 by 1 inch case. The SGI-100BT can adjust, split or recalibrate an electronic speed signal and calibrate a tach signal.
>
> It can also help create and adjust a gas-style tach signal for diesel swaps. An optional flywheel tooth sensor is sold here. A wiring and setup manual and an app are on the page.

### SGI-17 (p1103): CDI Ignition Tach Adaptor.

File: `data/descriptions/SGI-17-p1103.md`

**What was wrong:** no rewrite file; original copy only 26 words. Short on purpose: Page gives one fit sentence.

> Installing an aftermarket tach in a 1985-87 Buick Grand National with a CDI ignition? The SGI-17 tach adaptor makes it work with any aftermarket tachometer.

### SGI-20 (p1429): SGI-20: GMR TACH ADAPTER

File: `data/descriptions/SGI-20-p1429.md`

**What was wrong:** no rewrite file; banned: whether you're. Short on purpose: Page gives only how it works.

> Get a clean tach signal without cutting a wire. The SGI-20 uses a GMR, or giant magnetoresistance, pickup that clamps right onto a low-voltage, high-current wire.
>
> There's no splicing and no permanent change to your harness. It turns what it senses into a steady 12 volt square wave that modern gauges or engine management can read. Use it in a classic hot rod retrofit, a custom build or to fix a signal problem in the shop.

### SIM-1A-GL (p240): Electronic Speedometer Adjustment Module for Honda Goldwings

File: `data/descriptions/SIM-1A-GL-p240.md`

**What was wrong:** no rewrite file; original copy only 59 words. Short on purpose: Page gives only fit and use.

> Honda Gold Wing owners can correct the speedometer and odometer after changing tire size, pulley size or gearing. The SIM-1A-GL plugs into 1996-2017 speed sensor harnesses.
>
> It fits between the stock transmission sensor and the original speedometer, then tucks into the wiring after you adjust it.

### SIM-1A-M (p239): Electronic Speedometer Adjustment Module for Sportbike and Metric Crusiers.

File: `data/descriptions/SIM-1A-M-p239.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only use and size.

> Sportbikes and metric cruisers with electric speedometers can read true again after a tire, pulley or gearing change. The SIM-1A-M corrects both the speedometer and odometer.
>
> It splices in between the stock transmission sensor and the original speedometer, then hides in the harness after adjustment. The new version is smaller for easier mounting and can calibrate more bikes.

### SIM-1A (p1011): Electronic Speedometer Adjustment Module

File: `data/descriptions/SIM-1A-p1011.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only use, fit and size.

> Changed your tire size, pulley or gearing? The SIM-1A corrects your Harley's speedometer and odometer, and it stays in the harness for good.
>
> It plugs in where the stock Harley transmission sensor meets the original speedometer or the ECM, then tucks into the wiring once it's adjusted. The new version is smaller for easier mounting and has a wider correction range.

### STA-1000 (p825): OBD II Speedometer/ Tachometer Interface

File: `data/descriptions/STA-1000-p825.md`

**What was wrong:** no rewrite file; original copy only 37 words; exclamation point. Short on purpose: Page gives only the plug-in and outputs.

> Late-model drivetrain swaps get easier with the STA-1000. It plugs straight into the OBD II diagnostic connector.
>
> It puts out a traditional speedometer, tachometer and check engine signal that you can adjust, so you can run the aftermarket gauges you want.

### STM-100 (p735): Harley-Davidson Aftermarket Speedometer/ Tachometer Interface

File: `data/descriptions/STM-100-p735.md`

**What was wrong:** no rewrite file; exclamation point; banned: allows you to

> Run Dakota Digital or most aftermarket speedometers and tachs on a 2004 and up Harley-Davidson. The STM-100 reads the stock ECU's databus signal. It doesn't work on 2011 and newer Softails, 2012 and newer Dynas or 2014 and newer Road Kings.
>
> It outputs accessory power and ground, a tach signal you can set for 1, 2 or 4 cylinders, an 8,000 PPM speed signal and the check engine signal. A digital readout lets you read and clear trouble codes like a scan tool.
>
> It only makes an 8,000 PPM signal, so make sure your aftermarket speedometer can be adjusted before you order.

### TSI-1 (p247): Turn Signal Interface Module

File: `data/descriptions/TSI-1-p247.md`

**What was wrong:** no rewrite file; original copy only 42 words. Short on purpose: Page gives only fit and wiring.

> The TSI-1 lets HLY-1000, HLY-3000, MCL-5000 and HLY-5000 series speedometers work with automatic turn signal canceling modules.
>
> It needs only 12VDC, ground, a speed input and the turn signal output, so it's easy to hook up.

### VCM-101 (p1398): Velocity Cruise Commander for Drive by Wire (DBW) Throttle Bodies

File: `data/descriptions/VCM-101-p1398.md`

**What was wrong:** no rewrite file; exclamation point; banned: elevate

> Add cruise control to a newer drive-by-wire GM, Ford or Mopar drivetrain. The Velocity Cruise Commander works with OEM OBD-II/CAN or aftermarket EFI systems with electronic pedal control. It's engineered and built in Sioux Falls, South Dakota.
>
> The VCM-101 is for GM LS and LT engines with an inline 6-pin pedal harness, and the VCM-105 is for Ford and Mopar with an inline 6-pin harness. A setup wizard walks you through the install. An optional harness connects directly to Holley Dominator and Terminator X Max, FiTech LS and TCU, Haltech, ACES Quick Draw, AEM and MegaSquirt EFI.
>
> Cruise handles are sold separately. You can add the HND-8-C or HND-9-K when you order. An app for iOS and Android is on the page.

### VCM-200 (p1399): Velocity Cruise Control for Mechanical CableThrottle Bodies

File: `data/descriptions/VCM-200-p1399.md`

**What was wrong:** no rewrite file; semicolon; exclamation point; banned: elevate. Short on purpose: Page gives only the two versions, app and handles.

> Cable-operated throttle bodies get cruise control with the VCM-200 and VCM-300. The VCM-200 is for cable-driven speedometers, and the VCM-300 is for electronic speedometers.
>
> Set it up with the Dakota Digital app, which has a built-in setup wizard and a troubleshooting wizard. A speed sensor comes with the VCM-200. Add an HND-8-C or HND-9-K cruise handle when you order, or go without.

### VFD3-1005 (p225): VFD3-1005: Universal Single 6.75" Round, Digital Instrument

File: `data/descriptions/VFD3-1005-p225.md`

**What was wrong:** no rewrite file; original copy only 35 words

> One 6.75 inch round panel holds all six gauges in this Designer Series system. The bezel is now show-quality triple chrome, and the unit is 6.5 inches across.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VFD3-40C-O (p101): 1940 Chevy Original Bezel Digital Instrument System

File: `data/descriptions/VFD3-40C-O-p101.md`

**What was wrong:** no rewrite file; original copy only 47 words; semicolon

> Keep the look of the original 1940 Chevy dash housing and get six digital gauges inside it. This Series III system fits the original dash housing.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VFD3-41C (p102): 1941-48 Chevy Aluminum Bezel Digital Instrument System

File: `data/descriptions/VFD3-41C-p102.md`

**What was wrong:** no rewrite file; original copy only 33 words

> A billet aluminum dash housing comes with this five gauge Series III system for 1941-48 Chevys.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> A matching clock panel with a vacuum fluorescent clock is sold separately and has a limited lifetime warranty. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VFD3-69C-NOV (p203): 1969-76 Chevy Nova, 73-75 Buick Apollo, 75-76 Skylark, 73-76 Olds Omega, 71-76 Pontiac Ventura

File: `data/descriptions/VFD3-69C-NOV-p203.md`

**What was wrong:** no rewrite file; original copy only 40 words

> Six digital gauges fit the OEM bezel of a 1969-76 Nova with this Series III system. The title also lists the 1973-75 Apollo, 1975-76 Skylark, 1973-76 Omega and 1971-76 Ventura.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> It fits directly into your existing bezel, which isn't included. A metric version is a special order.

### VFD3-86C-S10 (p234): 1986-93 Chevy/ GMC S-10/ S-15 Pickups and 1986-94 S-10/ S-15 Blazers/ Jimmy's

File: `data/descriptions/VFD3-86C-S10-p234.md`

**What was wrong:** no rewrite file

> S-10 and S-15 pickups from 1986-93 and Blazers and Jimmys from 1986-94 can run six Series III digital gauges in the OEM bezel. On 1986-88 trucks, it fits those with factory oil pressure and water temp gauges, not warning lights.
>
> On 1989-93 trucks, it fits those with factory oil and water gauges and no factory tach. It won't fit trucks with warning lights or the factory digital dash. The bezel isn't included, so use an OEM or reproduction one.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VFD3-91C-CAP-A (p646): 1991-93 Chevy Caprice with Factory Analog Gauges

File: `data/descriptions/VFD3-91C-CAP-A-p646.md`

**What was wrong:** no rewrite file; original copy only 52 words

> Does your 1991-93 Caprice have factory analog gauges? This Series III system puts six digital gauges in its OEM bezel, using the OEM mounting hardware.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> It fits your existing bezel and mounting hardware, which aren't included. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VFD3-91C-CAP-D (p687): 1991-93 Chevy Caprice w/ OEM Digital Speedo, 91-93 Buick Roadmaster, 91-92 Olds Custom Cruiser

File: `data/descriptions/VFD3-91C-CAP-D-p687.md`

**What was wrong:** no rewrite file; original copy only 52 words

> This six gauge Series III system fits the 1991-93 Caprice with the factory digital speedometer, the 1991-93 Buick Roadmaster and the 1991-92 Olds Custom Cruiser.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> It fits directly into your existing bezel and mounting hardware, which aren't included. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VFD3X-1002 (p229): VFD3X-1002: Universal 3.5" x 19" Rectangle, Digital Instrument

File: `data/descriptions/VFD3X-1002-p229.md`

**What was wrong:** no rewrite file; original copy only 19 words. Short on purpose: Universal panel page: size and the shared spec only.

> Six digital gauges fill this universal 3.5 by 19 inch rectangle panel from the Designer Series.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VFD3X-1002B (p228): VFD3X-1002B: Universal 2" x 19" Oval, Digital VFD Instrument

File: `data/descriptions/VFD3X-1002B-p228.md`

**What was wrong:** no rewrite file; original copy only 19 words

> This universal 2 by 19 inch oval panel holds six digital gauges and comes with a bezel. Choose a brushed satin or chrome finish.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VFD3X-69C-IMP (p178): 1969-70 Chevy Caprice/Impala Digital Instrument System

File: `data/descriptions/VFD3X-69C-IMP-p178.md`

**What was wrong:** no rewrite file; original copy only 46 words; semicolon

> Six Series III digital gauges fit the OEM bezel of a 1969-70 Chevy Impala or Caprice.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> It uses your factory bezel, trim and fascia, which aren't included. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VFD3X-71C-IMP (p179): 1971-76 Chevy Caprice/ Impala Digital Instrument System

File: `data/descriptions/VFD3X-71C-IMP-p179.md`

**What was wrong:** no rewrite file; original copy only 46 words; semicolon. Short on purpose: Page gives only fit and the shared spec.

> A 1971-76 Impala or Caprice can run six Series III digital gauges in its OEM bezel.
>
> Its Series III vacuum fluorescent displays are bright, easy to read and accurate, in blue or teal. Speed reads to 255 mph and the tach to 17,500 rpm. The message centers add an odometer, two trip meters, a 0-60 timer, quarter-mile time and trap speed, and high speed and rpm recall.
>
> It uses your factory bezel, trim and fascia, which aren't included. A metric version is a special order.

### VHX-1019 (p845): VHX-1019: Universal Single 7" Round, Analog VHX Instrument

File: `data/descriptions/VHX-1019-p845.md`

**What was wrong:** no rewrite file; exclamation point

> Clean up the dash with one 7 inch gauge that does it all. It drops into a 6.75 inch hole from the front, and its chromed billet aluminum housing adds some flash. Leave two inches of depth behind the dash.
>
> Choose black alloy, silver alloy or carbon fiber look faces, with blue or red lighting. The speedometer reads to 160 mph and the tach to 8,000 rpm.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty. A metric version is a special order, and the BIM-01-2, DIM-1 and GSS-3000 are popular add-ons.

### VHX-1200 (p880): VHX-1200: 1967-69 Marquez Designs Camaro

File: `data/descriptions/VHX-1200-p880.md`

**What was wrong:** no rewrite file; original copy 171 words

> Built for the Marquez Design fiberglass dash in a 1967-69 Camaro, the VHX-1200 mixes race gauge function with street usability. The speedometer reads to 160 mph and the tach to 10,000 rpm, with large-sweep oil pressure, temperature, volt and fuel gauges.
>
> Four programmable message centers leave lots of room to add readings. The billet aluminum faceplate is powder-coated flat black and machined for a layered look. Choose black alloy, silver alloy or carbon fiber look faces.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty. A gear shift sender, dimming knob and OBD-II/CAN interface are optional add-ons.

### VHX-61L (p1063): 1961-63 Lincoln Continental

File: `data/descriptions/VHX-61L-p1063.md`

**What was wrong:** no rewrite file; original copy 165 words

> Big, classy 1961-63 Lincolns have become a favorite with car builders. This VHX system fills the three rectangular gauge bezels with six needles and two LCD message centers.
>
> It's a direct fit, but the inside of the stock instrument cluster has to be permanently modified for clearance. The mounting manual has the details. The stock housings and mounting plate aren't included. Choose black or silver alloy faces and blue, red or white lighting. A metric version is a special order.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-64L (p1114): 1964-65 Lincoln Continental

File: `data/descriptions/VHX-64L-p1114.md`

**What was wrong:** no rewrite file; original copy 221 words; semicolon; exclamation point

> The 1964-65 Lincoln Continental is classy and tough at the same time, and this VHX system gives it '60s style with modern technology. Use your stock dash bezels and trim.
>
> It connects to any drivetrain, from a stock 430 to an LS3 or anything in between. The bezel isn't included, so use your OEM or reproduction one. Choose black or silver alloy faces and blue, red or white lighting. A metric version is a special order.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-66L (p1115): 1966-69 Lincoln Continental

File: `data/descriptions/VHX-66L-p1115.md`

**What was wrong:** no rewrite file; original copy 230 words; semicolon; exclamation point

> Fill the three rectangular gauge bezels of a 1966-69 Lincoln with six needles and two LCD message centers. It doesn't fit the 1969 Mark III.
>
> It's a direct fit, but the inside of the stock instrument cluster needs some modification. The bezel isn't included, so use your OEM or reproduction one. Choose black or silver alloy faces and blue, red or white lighting. A metric version is a special order.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-68D-CHG (p939): 1968-70 Dodge Charger, Super Bee, Coronet R/T, 1970 GTX and Road Runner

File: `data/descriptions/VHX-68D-CHG-p939.md`

**What was wrong:** no rewrite file; semicolon; exclamation point

> Finally, a direct-fit, bolt-in VHX system for the 1968-70 Charger, Super Bee and Coronet R/T, plus the 1970 GTX and Road Runner. Its billet aluminum housing bolts to the original bezel, which isn't included.
>
> Six analog sweep gauges come with matching LCD message centers, and the turn signals use their original spots with LED lighting. Choose black or silver alloy faces and blue, red or white lighting. A metric version is a special order.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-68D-STD (p1164): 1968-70 Mopar B-Body: Coronet, Belvedere, Satellite and Road Runner

File: `data/descriptions/VHX-68D-STD-p1164.md`

**What was wrong:** no rewrite file; semicolon; exclamation point

> Mopar B-bodies from 1968-70 without the rallye dash get this direct-fit VHX package. It uses your stock instrument surround and dash pad, so the install is easy.
>
> Six analog sweep gauges and one large LCD message center show more than the original ever did, and the key indicators are built in. The bezel isn't included. Choose black or silver alloy faces and blue, red or white lighting. A metric version is a special order.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-69C-NOV (p815): 1969-76 Chevy Nova, 73-75 Buick Apollo, 75-76 Skylark, 73-76 Olds Omega, 71-76 Pontiac Ventura

File: `data/descriptions/VHX-69C-NOV-p815.md`

**What was wrong:** no rewrite file; exclamation point. Short on purpose: Page gives only fit, bezel note and options.

> Get full gauge readouts in the stock spot of a 1969-76 Nova or one of its clones. This compact VHX system uses your original or reproduction bezel.
>
> It fits the factory bezel, which isn't included. Choose black alloy, silver alloy or carbon fiber look faces and blue or red lighting. A metric version is a special order.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-70D-CLG (p1027): 1970-74 Dodge Challenger and 1970-74 Plymouth Cuda with Rallye dash

File: `data/descriptions/VHX-70D-CLG-p1027.md`

**What was wrong:** no rewrite file; original copy 167 words; semicolon

> A 426 Hemi under the shaker hood made the 1970 'Cuda a legend. This bolt-in six gauge VHX system fits 1970-74 Challengers and 'Cudas with the rallye dash.
>
> It replaces the original instrument housing and lens and uses your stock gauge bezel, which isn't included. Twin LCD message centers show extra readings, and turn signals and brake indicators now light with LEDs in the original spots. Choose black or silver alloy faces and blue, red or white lighting. A metric version is a special order.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-70D-STD (p1165): 1970-74 Mopar E-Body: Challenger & Barracuda

File: `data/descriptions/VHX-70D-STD-p1165.md`

**What was wrong:** no rewrite file; semicolon

> Non-rallye 1970-74 Challengers and Barracudas get VHX technology with this bolt-in system. Included hardware fits the early stepped front bezel and the later flat one.
>
> Six analog readings flank twin LCD message centers, with built-in LED indicators. EFI hookup is easy with the BIM-01-2, sold separately. The bezel isn't included. Choose black or silver alloy faces and blue, red or white lighting. A metric version is a special order.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-73F-PU (p914): 1973-79 Ford Pickup, 78-79 Bronco

File: `data/descriptions/VHX-73F-PU-p914.md`

**What was wrong:** no rewrite file; semicolon; exclamation point

> Ford's 1973-79 F-Series trucks are more popular than ever, and this VHX upgrade uses the stock gauge bezel and hardware. It also fits 1978-79 Broncos, but not the E-Van.
>
> Six analog gauge readouts and twin LCD message centers cover everything. The bezel isn't included. Choose black alloy, silver alloy or carbon fiber look faces and blue or red lighting. A metric version is a special order.
>
> VHX gives you lit needles, backlit faces and LCD message centers, driven by stepper motors with solid-state sensors. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VLC-16-1 (p1013): 3" Round Universal VHX Clock

File: `data/descriptions/VLC-16-1-p1013.md`

**What was wrong:** no rewrite file; semicolon; exclamation point. Short on purpose: Page gives only lighting, size, options and fit.

> A real analog clock with hands to match your VHX gauges. LED backlighting lights both hands, even though they ride on the same stepper motor.
>
> It needs a 2-3/4 inch cutout and is 3 inches across, in a chromed billet aluminum housing. Choose black alloy, silver alloy or carbon fiber look faces and blue, red or white lighting. It only works with VHX systems, not on its own or with VFD3 digital systems.

### VLC-16-2 (p1227): 2-1/16" Round Universal VHX Clock

File: `data/descriptions/VLC-16-2-p1227.md`

**What was wrong:** no rewrite file. Short on purpose: Page gives only size, match, options and standalone note.

> This universal VHX clock mounts in a small 2-1/16 inch hole. Its bezel shape and 2-5/16 inch overall size match the VHX-1024, VHX-1050 and VHX-1060 packages.
>
> Choose black or silver alloy faces and blue, red or white lighting. It has to connect to a VHX control box and can't be used as a standalone clock.

### XMT-4 (p81): 4-Button Replacement Transmitter

File: `data/descriptions/XMT-4-p81.md`

**What was wrong:** no rewrite file; no description on the page. Short on purpose: No description on the page: title and item name only.

> This is a replacement remote transmitter. The page title calls it a 4-button transmitter, and the item is listed as a four-function remote replacement.

### XMT-6-9K (p694): 6-Button Replacement Transmitter

File: `data/descriptions/XMT-6-9K-p694.md`

**What was wrong:** no rewrite file; original copy only 11 words. Short on purpose: Page gives only fit and manual.

> This 6-button replacement transmitter works with the CMD-9000 only. A programming manual is on the page.

### XMT-6 (p80): 6-Button Replacement Transmitter

File: `data/descriptions/XMT-6-p80.md`

**What was wrong:** no rewrite file; original copy only 10 words. Short on purpose: Page gives only fit and manual.

> The XMT-6 is a 6-button replacement transmitter for the CMD-10K remote system. A programming and setup manual is on the page.

### (no SKU) (p1105): Product 1105 (no longer listed)

File: `data/descriptions/p1105.md`

**What was wrong:** no rewrite file; original copy only 31 words. Short on purpose: Discontinued placeholder page.

> You've reached an item Dakota Digital has taken off its site. It may be discontinued or replaced. Search for a current part above, or ask the team what replaced it.

### (no SKU) (p1127): Product 1127 (no longer listed)

File: `data/descriptions/p1127.md`

**What was wrong:** no rewrite file; original copy only 31 words. Short on purpose: Discontinued placeholder page.

> Sorry, this part isn't listed anymore. It may have been discontinued or replaced. Try the search above, or contact Dakota Digital to ask what took its place.

### (no SKU) (p214): Custom Mounted Instruments -Uses OEM Gauge Housing

File: `data/descriptions/p214.md`

**What was wrong:** no rewrite file; original copy 234 words; semicolon

> Can't find a stock system that fits, or have an idea for something custom? Dakota Digital's craftsmen can build a system into the gauge housing from your car or truck. Choose HDX for analog faces with a color screen, or VFD for a dark face lit with digital readings.
>
> You can match colors to your interior, even from a sample you send, and add custom graphics. Both cost extra. HDX custom gauges start at $3,000, and current lead times are about 4 months.
>
> Your stock housing must be usable and already finished, since painting, chrome and polishing aren't offered. Send the OEM gauges and clear lenses so every dimension is right, and unused parts come back to you. Pack everything well, because Dakota Digital isn't liable for shipping damage.

### (no SKU) (p216): Digital Clock Custom Mounted into Original Bezel

File: `data/descriptions/p216.md`

**What was wrong:** no rewrite file; exclamation point. Short on purpose: Page gives only the service, prep steps, ordering, warranty and colors.

> Keep the original look and get a digital clock. Dakota Digital's custom shop can rebuild your OEM clock with a vacuum fluorescent display, using your stock clock housing.
>
> Send in the original housing, and the shop handles the fabrication and mounting at the factory. Finish the bezel or housing first, just as you would for the car, with paint, chrome or polish. Contact Dakota Digital with any questions about your dash.
>
> Call to order. It's covered by a limited lifetime warranty, and the standard colors are blue or teal.

### ODYR/SLX-01-1 (p285): Round 3-3/8" Performance Speedometer

File: `data/descriptions/p285.md`

**What was wrong:** no rewrite file; original copy only 37 words; semicolon. Short on purpose: Gauge page: range, sensor, options and warranty only.

> This 3-3/8 inch round performance speedometer is part of the Odyssey Series II and Solarix line.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects. It ships with 0 miles on the odometer, and the factory can set your mileage for $20.

### ODYR/SLX-02-1 (p287): Round 3-3/8" Performance Tachometer

File: `data/descriptions/p287.md`

**What was wrong:** no rewrite file; original copy only 14 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Here's a 3-3/8 inch round performance tachometer from the Odyssey Series II and Solarix line.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-01-6 (p289): Performance 3-3/8" Speedometer/Tachometer

File: `data/descriptions/p289.md`

**What was wrong:** no rewrite file; original copy only 37 words; semicolon. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Speed and tach share one 3-3/8 inch round performance gauge here, in the Odyssey Series II and Solarix style.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects. It ships with 0 miles on the odometer, and the factory can set your mileage for $20.

### ODYR/SLX-01-3 (p292): Mini 2-1/16" Speedometer

File: `data/descriptions/p292.md`

**What was wrong:** no rewrite file; original copy only 37 words; semicolon. Short on purpose: Gauge page: range, sensor, options and warranty only.

> A 2-1/16 inch mini speedometer in MPH or KPH, from the Odyssey Series II and Solarix line.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects. It ships with 0 miles on the odometer, and the factory can set your mileage for $20.

### ODYR/SLX-02-7 (p294): Mini 2-1/16" Tachometer

File: `data/descriptions/p294.md`

**What was wrong:** no rewrite file; original copy only 14 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> This 2-1/16 inch mini tachometer comes in the Odyssey Series II and Solarix styles.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-23-1 (p308): 2-1/16" Nitrous Pressure

File: `data/descriptions/p308.md`

**What was wrong:** no rewrite file; original copy only 21 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Nitrous bottle pressure reads 0-2000 psi on this 2-1/16 inch gauge. It needs the SEN-23-1 sensor.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-50-1 (p311): 5 Gauge Kit

File: `data/descriptions/p311.md`

**What was wrong:** no rewrite file; original copy only 58 words; semicolon

> This 5 gauge Odyssey Series II and Solarix kit comes with wiring manuals for the speedometer and tach, oil pressure, water temp, voltmeter and fuel level gauges.
>
> The oil pressure, water temp and speed senders are included. The fuel gauge reads an OEM or aftermarket sensor in most cars.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Bezels come in black or chrome, and it carries a limited 24-month warranty against manufacturer defects. It ships with 0 miles on the odometer, and the factory can set your mileage for $20.

### ODYR/SLX-60-1 (p313): 6 Gauge Kit

File: `data/descriptions/p313.md`

**What was wrong:** no rewrite file; semicolon; exclamation point

> Get six Odyssey gauges in one kit, with manuals for the speedometer, tach, oil pressure, water temp, voltmeter and fuel level. The vacuum fluorescent displays are bright and easy to see in daylight.
>
> Oil pressure, water temp and speed senders come in the box. The fuel gauge works with an OEM or aftermarket sensor in most cars.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Bezels come in black or chrome, and it carries a limited 24-month warranty against manufacturer defects. It ships with 0 miles on the odometer, and the factory can set your mileage for $20.

### ODYR/SLX-14-1 (p315): 2-1/16" Ambient Air Temp

File: `data/descriptions/p315.md`

**What was wrong:** no rewrite file; original copy only 25 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Outside air temperature shows on this 2-1/16 inch gauge, from -40 to 250 degrees F or -40 to 120 degrees C. It needs the SEN-15-1 sensor.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-15-1 (p319): 2-1/16" Amplifier Temp

File: `data/descriptions/p319.md`

**What was wrong:** no rewrite file; original copy only 26 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Keep an eye on amplifier temperature with this 2-1/16 inch gauge. It reads -40 to 250 degrees F or -40 to 120 degrees C and needs the SEN-15-1 sensor.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-03-1 (p322): 2-1/16" Oil Pressure

File: `data/descriptions/p322.md`

**What was wrong:** no rewrite file; original copy only 25 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Oil pressure shows from 0-150 psi, in 1 psi steps, on this 2-1/16 inch gauge. A sender is required and sold separately, in 1/8 inch NPT or 10mm.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-07-3 (p326): 2-1/16" Oil Temperature

File: `data/descriptions/p326.md`

**What was wrong:** no rewrite file; original copy only 27 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> This 2-1/16 inch gauge reads oil temperature from 0-400 degrees F or 0-200 degrees C, in 1 degree steps. It needs the SEN-04-3 sender, sold here.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-09-5 (p332): 2-1/16" Vacuum/ Boost

File: `data/descriptions/p332.md`

**What was wrong:** no rewrite file; original copy only 27 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Vacuum and boost read from 30 inHg to 80 psi on this 2-1/16 inch gauge, in 1 inHg or 0.2 psi steps. The sender is now included and mounts right on the manifold.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-12-1 (p345): 2-1/16" Exhaust Gas Temperature

File: `data/descriptions/p345.md`

**What was wrong:** no rewrite file; original copy only 28 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> This 2-1/16 inch pyrometer reads exhaust gas temperature from 150-1750 degrees F or 65-955 degrees C, in 10 degree F or 5 degree C steps. A probe is required, with 6, 10, 14 or 18 ft leads.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-11-1 (p347): 2-1/16" Cylinder Head Temperature

File: `data/descriptions/p347.md`

**What was wrong:** no rewrite file; original copy only 30 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Cylinder head temperature reads 150-750 degrees F or 65-400 degrees C on this 2-1/16 inch gauge, in 4 degree F or 3 degree C steps. A sensor is required, with leads from 6 to 18 ft, and an 18 ft sender for 14mm spark plugs is listed too.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-06-1 (p349): 2-1/16" Fuel Level

File: `data/descriptions/p349.md`

**What was wrong:** no rewrite file. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Fuel level reads 0-99% on this 2-1/16 inch gauge. It's preset for GM30, GM90, GM250, Ford10, Ford150, VDO, Stewart Warner/Sun and Import senders, and the SEN-06-1 universal sensor fits most tanks.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-05-1 (p358): 2-1/16" Voltmeter

File: `data/descriptions/p358.md`

**What was wrong:** no rewrite file; original copy only 21 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Volts read 1-17.0 on this 2-1/16 inch gauge, in 0.1 volt steps.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-20-5 (p360): 2-1/16" Amp Current

File: `data/descriptions/p360.md`

**What was wrong:** no rewrite file; original copy only 33 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Current reads 0-250 amps on this 2-1/16 inch gauge, in 1 amp steps. It needs the SEN-20-3 amp current sensor, sold separately.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-04-1 (p363): 2-1/16" Water Temperature

File: `data/descriptions/p363.md`

**What was wrong:** no rewrite file; original copy only 24 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> The 2-1/16 inch water temperature gauge reads 0-300 degrees F or 0-150 degrees C, in 1 degree steps. Senders are sold in 1/8, 3/8 and 1/2 inch NPT and 12, 14 and 16mm.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-08-3 (p365): 2-1/16" Transmission Temperature

File: `data/descriptions/p365.md`

**What was wrong:** no rewrite file; original copy only 24 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> Transmission temperature reads 0-400 degrees F or 0-200 degrees C on this 2-1/16 inch gauge. The SEN-04-3 sender and inline sender blocks for 5/16 or 3/8 inch lines are sold here, and the sender is separate from the blocks.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-40-1 (p368): 3-3/8" Fuel/ Volts/ Oil Pressure/ Water Temperature

File: `data/descriptions/p368.md`

**What was wrong:** no rewrite file; original copy only 38 words. Short on purpose: Thin page: little beyond the part list or one-line description.

> Fuel, volts, oil pressure and water temperature share one 3-3/8 inch gauge in this Odyssey Series II and Solarix design. Water temp reads 0-300 degrees F or 0-150 degrees C, in 1 degree steps.
>
> The water temp and oil pressure senders are now included. The fuel sender is sold separately.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Bezels come in black or chrome, and it carries a limited 24-month warranty against manufacturer defects.

### ODYR/SLX-19-1 (p389): 2-1/16" Air Pressure

File: `data/descriptions/p389.md`

**What was wrong:** no rewrite file; original copy only 44 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> This 2-1/16 inch air pressure gauge reads 0-150 or 0-400 psi, depending on the sender. Resolution is 1 psi on the lower range and 2 psi on the higher one. Both senders are sold here.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### (no SKU) (p392): Motorcycle Technical Manuals

File: `data/descriptions/p392.md`

**What was wrong:** no rewrite file; no description on the page. Short on purpose: Manual index page: tabs and model list only.

> Find the manuals for Dakota Digital motorcycle gauges here, sorted into current, UTV and legacy tabs.
>
> The Harley-Davidson replacement gauge list shows the current and prior manual versions for each model, with a short description. It covers the MLX-2000, 2004 and 2011 tank mount gauges and the MLX-3000, 3004 and 3012 gauges, along with others.

### (no SKU) (p393): Automotive Technical Manuals

File: `data/descriptions/p393.md`

**What was wrong:** no rewrite file; original copy only 27 words. Short on purpose: Manual index page: tabs and section list only.

> Download the manual for your Dakota Digital automotive product from this page.
>
> Manuals are sorted into tabs for current products, GRFX, RTX, HDX, VHX, VFD, LED and legacy products. Many products list both a current and a prior version.
>
> For example, the Commander remote systems section covers the CMD-2000, CMD-4000, CMD-10K and CMD-X, along with the Magnum Shooters, the PDR-2 solenoid, the relays and the XMT-6 transmitter.

### ODYR/SLX-10-2 (p397): 2-1/16" High Resolution Fuel Pressure

File: `data/descriptions/p397.md`

**What was wrong:** no rewrite file; original copy only 57 words. Short on purpose: Gauge page: range, sensor, options and warranty only.

> This 2-1/16 inch gauge shows high resolution fuel pressure from 0-100 psi. It needs the SEN-09-4 sensor. On diesels, add a snubber adaptor before the sensor to protect it from pressure spikes.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Both come with a black or chrome bezel, are built in house and carry a limited 24-month warranty against manufacturer defects.

### HND-9-C Coming Soon! (p49): VCM Series Dash-Mounted Cruise Control Switch

File: `data/descriptions/p49.md`

**What was wrong:** no rewrite file; em dash. Short on purpose: Page gives only fit, size, finishes, warranty and manual.

> The HND-9 cruise control switch mounts on the dash and works only with Dakota Digital VCM series cruise systems. It isn't made for OEM or CRC/CRS systems.
>
> It's CNC-machined from aluminum and measures 2.05 by 1.45 inches, small enough to tuck out of the way. Choose a chrome or black outer housing. The chrome version is listed as coming soon.
>
> It has a 5-year warranty. A wiring and setup manual is on the page.

### ODYR/SLX-61-1 (p574): Dual 3-3/8" Round Gauge Kit

File: `data/descriptions/p574.md`

**What was wrong:** no rewrite file. Short on purpose: Thin page: little beyond the part list or one-line description.

> Two 3-3/8 inch round gauges make up this kit: a performance speedometer and tach, plus a combined fuel, volts, oil pressure and water temp gauge.
>
> Water temp reads 0-300 degrees F or 0-150 degrees C, in 1 degree steps. The water temp and oil pressure senders are now included, and the fuel sender is sold separately.
>
> Pick Odyssey Series II for a non-glare teal display with neon green labels, or Solarix for a high-contrast blue display with blue labels. Bezels come in black or chrome, and it carries a limited 24-month warranty against manufacturer defects.

### (no SKU) (p600): Product 600 (no longer listed)

File: `data/descriptions/p600.md`

**What was wrong:** no rewrite file; original copy only 31 words. Short on purpose: Discontinued placeholder page.

> Dakota Digital no longer lists this item, so it may be discontinued or replaced. Use the search above to find a current part, or contact the team to ask what took its place.

### MVX-8K-A + MBM-19 (p928): MVX A La Carte Bagger Gauges

File: `data/descriptions/p928.md`

**What was wrong:** no rewrite file; exclamation point

> Build your own MVX bagger gauge set. Start with the MVX-820x speedometer and tach pair, which every a la carte setup needs, then add gauges up to a total of 7. Run just 4 if you need room for tweeters.
>
> Auxiliary gauges cover fuel level, oil pressure, oil temp and voltage, with chrome or black bezels and a black or white face with gray. Gauges come in 1996-03 and 2004-up versions. The air pressure gauge comes with the MBM-19 module and one sensor, and the boost gauge comes with the MBM-09 and its sensor.
>
> Want more readings without another gauge? Plug in an MBM module to show boost, air pressure or compass in the speedometer and tach message centers.

### (no SKU) (p948): MCL-3014 and MCL-3014-R

File: `data/descriptions/p948.md`

**What was wrong:** no rewrite file; original copy 290 words; exclamation point

> Bright blue or red digital readouts come to 2014-2018 Harley-Davidson touring bikes with the MCL-3014. It fits the Road Glide, Street Glide, Tri Glide, Ultra Limited and every CVO, with readouts that are easier to see than the OEM gauges. It doesn't fit 2019 and newer models.
>
> It uses the stock chrome trim rings. Add readings in the odometer, trip or clock displays, or swap the oil temp gauge for an air pressure or boost gauge. Either way you need an MBM module: the MBM-19 for air pressure or the MBM-09 for boost. With either gauge, the oil temp reading goes away. A second pressure needs another SEN-1901 sender.
>
> Air and boost gauges need a base unit with software code MC14 or higher. Dakota Digital can update older units sent in for service. To buy, call 1-800-593-4160 or a dealer.

## Earlier rewrites reworded (carried-over wording)

These had at least one run of 12 or more words copied from the original copy, mostly the series boilerplate. The facts are unchanged; only the wording is new.

### GRFX-2017 (p1351): GRFX-2017: Universal 5.75" x 12" Elliptical, Digital GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Building a one-off dash? This universal GRFX cluster puts six simulated analog readings on three TFT displays inside a 12 by 5.7 inch elliptical body. Any gauge position can read out in analog, digital or bar-graph form, and you pick the theme, colors and warning modes.
>
> A billet aluminum front bezel is built into a 2 inch deep, black powdercoated housing, so it's one piece. The cutout is 11.655 by 5.295 inches, and you need two inches of clearance behind it. The sensors are included with full-length harnesses. Backup cameras, which the largest screen can show, are sold separately.
>
> A built-in rotary switch keeps installation simple. GPS calibrates the speedometer, Bluetooth links the Dakota Digital app, and a USB port takes updates. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### GRFX-3100 (p1403): GRFX-3100: Universal Competition, Digital GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Competition-style looks in a compact package: the GRFX-3100 packs a lot of information into its TFT screen. Any gauge position can read out in analog, digital or bar-graph form, and you pick the theme, colors and warning modes.
>
> It measures 10.75 by 6 inches overall and needs a 10.25 by 5.5 inch cutout, plus two inches of clearance behind it. The sensors are included with full-length harnesses. Backup cameras, which the screen can show, are sold separately.
>
> A built-in rotary switch keeps installation simple. GPS calibrates the speedometer, Bluetooth links the Dakota Digital app, and a USB port takes updates. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### GRFX-47C-PU (p1389): GRFX-47C-PU: 1947-53 Chevy/GMC Pickup GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Bright new chrome bezels fill the two round openings in a 1947-53 Chevy or GMC truck, with GRFX graphic gauges under the lenses. Every gauge position can show an analog, digital or bar-graph readout, and you set the theme, colors and warning modes. A G-force meter shows the forces as you corner, launch and brake.
>
> It works with anything from an old-school engine to the latest fuel injection. The sensors are in the box, each with a full-length harness. The largest screen can show a backup camera, sold separately. Each camera includes a universal mount and a full-length harness.
>
> Built-in GPS calibrates the speedometer for your tire size and gearing. Bluetooth connects the Dakota Digital app for setup and live data, and the USB port takes updates. A separate control module keeps wiring tidy. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### GRFX-55C-PU (p1359): GRFX-55C-PU: 1955-59 Chevy Pickup, GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A backlit billet aluminum knob in the face of this cluster runs the whole show. Turn it to change readouts and reset timers, or go deeper for calibration and display setup. Any gauge position can read out in analog, digital or bar-graph form, and you pick the graphic theme and colors.
>
> It drops into the OEM front gauge bezel of a 1955-59 Chevy truck. The bezel isn't included, so use an OEM or reproduction one. It works with anything from the original engine to the latest LT power. The sensors come with full-length harnesses, and backup cameras are sold separately.
>
> Built-in GPS calibrates the speedometer for your tires and gearing. Bluetooth connects the Dakota Digital app, and a USB port takes updates. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### GRFX-60C-PU (p1388): GRFX-60C-PU: 1960-63 Chevy Pickup GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> First-gen 1960-63 Chevy C/K trucks can now run the GRFX series of gauges. Pick a graphic theme, then set the colors and warning modes for each element. A gauge position can show one reading, two at once, or something else entirely. The largest screen can also show a backup camera.
>
> It uses your OEM or reproduction bezel, which isn't included. Backup cameras are sold separately and include a universal mount and a full-length harness. The water temperature probe, oil pressure sender and speedometer pulse generator are all in the box.
>
> GPS sets the speedometer for you, so there's nothing to calibrate by hand. A G-force meter shows the pull when you corner, launch and brake. A separate control module keeps the wiring tidy, and the whole system is built in Sioux Falls, South Dakota.

### GRFX-66C-CVL (p1400): GRFX-66C-CVL: 1966-67 Chevy Chevelle/ El Camino GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Four high-resolution TFT screens fill the long sweep dash of a 1966-67 Chevelle. Any gauge position can read out in analog, digital or bar-graph form, and you pick the theme, colors and warning modes. The largest screen can also show a backup camera.
>
> It's a direct fit for the 1966-67 Chevelle and El Camino. It uses your OEM or reproduction bezel, which isn't included, and a replacement bezel is listed with this kit. Backup cameras are sold separately. The sensors come with full-length harnesses.
>
> Built-in GPS calibrates the speedometer for your tires and gearing. The Dakota Digital app connects over Bluetooth, and a USB port takes updates. A G-force meter shows the forces when you corner, launch and brake. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### GRFX-67C-CAM (p1394): GRFX-67C-CAM: 1967-68 Camaro/ Firebird GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Bring GRFX graphic gauges to a first-gen 1967-68 Chevy Camaro or Pontiac Firebird. Any gauge position can read out in analog, digital or bar-graph form, one reading or two. Start from a graphic theme, then pick colors and warning modes for every reading.
>
> The largest screen can also show a backup camera. Cameras are sold separately with a full-length harness and a universal mount. The box includes the sensors: a solid-state oil pressure sender, a speedometer pulse generator and a water temperature probe with adapter bushings.
>
> Built-in GPS keeps the speedometer calibrated for your tires and gearing. Bluetooth connects the Dakota Digital app, and a USB port takes updates. A G-force meter shows the forces when you corner, launch and brake. A separate control module keeps wiring tidy, and the system is built in Sioux Falls, South Dakota.

### GRFX-67C-PU (p1387): GRFX-67C-PU: 1967-72 Chevy Pickup GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The GRFX cluster fills your 1967-72 C10 bezel with graphic gauges you can set up your way. Every gauge position can show one reading, two at once, or a different reading entirely, as a needle, a number or a bar graph. Choose a theme, then pick the colors and warning modes yourself.
>
> It works with the original engine or the latest fuel injection you put under the hood. A replacement bezel for these trucks is listed with this kit. The largest screen can show a backup camera, sold separately. The included sensors each come with a full-length harness.
>
> GPS inside the cluster calibrates the speedometer for your tires and gears on its own. Use the Dakota Digital app over Bluetooth for setup and live sensor data, and load updates through the USB port. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### GRFX-70C-CAM (p1435): GRFX-70C-CAM: 1970-81 Chevy Camaro GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1970-81 Camaro's European-inspired cockpit was full of driver-focused gauges, and GRFX swaps them for full-digital TFT displays. You can customize them down to the last detail, from graphic themes and display colors to how each gauge position shows its reading.
>
> It bolts right in. The bezel isn't included. An optional backup camera, sold separately, shows right in the cluster. Each included sensor comes with a full-length harness.
>
> Set it up over Bluetooth with the Dakota Digital app. Built-in GPS calibrates the speedometer for your tires and gearing, a USB port takes updates, and a G-force meter shows cornering, launch and braking forces. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### GRFX-73C-PU (p1357): GRFX-73C-PU: 1973-87 Chevy Pickup, 1973-91 Chevy Blazer, GMC Jimmy and Suburbans GRFX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Each gauge spot in this cluster can show an analog, digital or bar-graph readout, and you decide which. Start from a graphic theme, then set colors and warning modes for each piece. The largest screen can also show a backup camera, and a built-in G-force meter shows what's happening when you corner, launch and brake.
>
> It bolts directly into 1973-87 Chevy pickups and 1973-91 Chevy Blazer, GMC Jimmy and Suburban dashes, and it works with any drivetrain. Backup cameras are sold separately and include a universal mount and a full-length harness. The sensors are in the box, each with a full-length harness.
>
> Built-in GPS calibrates the speedometer for your tire size and gearing, so there's nothing to set by hand. Bluetooth links the Dakota Digital app for setup and troubleshooting, and a USB port takes updates. A separate control module keeps wiring at the cluster tidy.

### HDX-2017 (p1075): HDX-2017: Universal 5.75" x 12" Elliptical, Analog HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Building a custom dash from scratch? This one-piece universal HDX cluster puts six analog readings and a large TFT message center in a 12 by 5.7 inch elliptical body. You choose black or silver alloy faces and your own lighting colors.
>
> A billet aluminum front bezel is built into the 2 inch deep housing. The cutout is 11.655 by 5.295 inches, and you need two inches of clearance behind it.
>
> Built-in touch switches make installation easier, and the Bluetooth app for iPhone and Android handles setup too. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-2018 (p1074): HDX-2018: Universal 4.4" x 11.4" Rounded Rectangle, Analog HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> For a custom interior, this universal HDX cluster fits six analog gauge readings and a large, full-color TFT message center. It measures 11.4 inches wide and 4.4 inches tall and sits just two inches deep behind the dash. Pick black or silver alloy faces and separate lighting colors for the readings, needles and message centers.
>
> The cutout is 11 by 4 inches. The housing and built-in front bezel are billet aluminum with show chrome plating. It works with BIM-series modules, and the sending units are supplied.
>
> Set it up with the built-in touch buttons or the Bluetooth app for Apple and Android. Indicators stay hidden until they light, and each gauge has its own settable red warning light. A central control box pulls signals from the vehicle harness.

### HDX-2024 (p1201): HDX-2024: Universal 6 Gauge Round, Analog HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Common aftermarket openings of 4-5/8 and 2-1/16 inches take this universal six-gauge HDX package, with chrome-plated billet aluminum housings. Upgrading an existing dash panel has never been easier.
>
> The gauges drop in from the front. The front bezels measure 5 inches across for the speedometer and tach and 2-5/16 inches for the satellites, and all need about 2-1/4 inches of depth. You get 30 backlighting colors, TFT displays and the control box. Faces come in black or silver alloy. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Water temperature, oil pressure and speed sensors come with 10 ft harnesses.

### HDX-2100 (p1144): HDX-2100: Universal Competition Analog HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Ready for a race-oriented gauge system? The universal HDX-2100 has a flat-black powdercoated billet aluminum faceplate with machining that gives a multi-layered look, plus exposed stainless hardware. Dual TFT message centers can be set up by the driver for nearly anything.
>
> It measures 10.75 by 5.875 inches overall and needs a 10.25 by 5.5 inch cutout. The tach reads to 10,000 rpm. Faces come in black or silver alloy. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-2200 (p1145): HDX-2200: Universal 6 Gauge Competition Analog HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Set your project apart with the universal HDX-2200. This six-gauge system has two large TFT message centers, with the touch programming switches just below them, and a 10,000 rpm tach.
>
> It needs 15.10 by 6.25 inches of flat dash space, a 14.60 by 5.83 inch cutout and 2 inches of clearance behind. The billet aluminum bezel is powdercoated matte black. Faces come in black or silver alloy. A metric version is a special order.
>
> You can also set it up with the Bluetooth app for iPhone and Android. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-47C-PU (p1036): 1947-53 Chevy/ GMC Pickup HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> No adapter rings or tiny round gauges here. Chrome-plated, machined aluminum housings replace the stock bezels and fit exactly into a stock 1947-53 Chevy or GMC pickup dash. Each gauge has a full-color TFT display and a pair of touch buttons, so you can set it up your way.
>
> The machined aluminum and chrome bezel is included. The system needs a 5.2 inch opening and measures 5.95 inches overall, and the depth usually matches the stock cluster. Fitting it to a different vehicle? Make any changes to the dash, not the HDX system, to keep warranty coverage. Faces come in black or silver alloy. A metric version is a special order.
>
> You can also set it up with the Bluetooth app for iPhone and Android. A central control box pulls signals from the truck's harness and connects the included solid-state senders.

### HDX-53C (p1087): 1953-54 Chevy Car HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> One large TFT message center sits between six analog instruments in this all-in-one HDX system for the 1953-54 Chevy car. A machined housing is made to fit the stock instrument bezel. Choose black or silver alloy faces.
>
> You'll need to open up a small section of the stock dash. The bezel isn't included, so use an OEM or reproduction one. The supplied sensors connect to your drivetrain. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android, and pick your lighting colors. Each gauge gets its own red warning light you can set, and a central control box takes signals from the car's harness.

### HDX-53F-PU (p1083): 1953-55 Ford Pickup HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The trapezoid-shaped cluster of a 1953-55 F100 finally has an answer. A new bezel is milled from solid aluminum to match the stock dash, then chromed. It holds six analog instruments and a large TFT message center. Faces come in black or silver alloy.
>
> The reproduction chrome bezel is included. The included sensors let it monitor your choice of drivetrain. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. Set it up with the touch buttons or the Bluetooth app for iPhone and Android. A central control box keeps the wiring simple.

### HDX-54C-PU (p1092): 1954 Chevy Pickup HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Skip adapter rings and "good enough." Custom-machined billet aluminum bezels fit the stock dash of 1954 and 1955 First Series Chevy pickups, with six analog instruments and twin TFT message centers. Choose black or silver alloy faces.
>
> Mounting hardware is supplied. It doesn't fit GMC. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android, and pick your lighting colors. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-55C-PU (p1037): 1955-59 Chevy Pickup HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Builders have put the V-shaped 1955-59 Chevy pickup cluster in plenty of custom dashes, and it still looks right in the trucks it came in. This HDX system fills it with six analog gauges and a single TFT display in the center that shows exactly the information you want. You pick black or silver alloy faces and separate lighting colors for the readings, needles and message centers.
>
> Mount it with a stock or reproduction bezel, sold separately. It doesn't fit GMC. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Indicators stay hidden until they light, and each gauge has its own red warning light you can set. A central control box connects the included solid-state senders, which keeps the install simple.

### HDX-55C (p1033): 1955-56 Chevy Car HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Six analog gauges fill the stock '55-56 Chevy dash, and a large TFT display adds more readings on top of them. Pick black or silver gauge faces. Then set your own lighting colors for the readings, the needles and the message center.
>
> It installs in your stock or reproduction bezel. The bezel isn't included, and reproduction chrome pieces are sold separately. So is the HLC clock, which is made to go with this system and isn't meant to be used alone. The system replaces the stock automatic gear indicator above the steering column, so add a gear shift sensor (sold separately) to show gear position. A metric version is a special order.
>
> Setup uses touch buttons in the face or the Bluetooth app for Apple and Android. A central control box pulls signals from the car's harness and connects the included solid-state senders, which makes the install much simpler.

### HDX-56F-PU (p1078): 1956 Ford Pickup HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The one-year 1956 F-series, with its built-in visor over the wraparound windshield, gets six analog instruments and a single TFT message center with this HDX package. Faces come in black or silver alloy, with lighting colors you choose.
>
> It bolts directly to a stock or reproduction bezel, which isn't included. The supplied sensors and available modules let it work with any drivetrain combination. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. Use the built-in touch buttons or a Bluetooth app on iPhone or Android for setup. A central control box keeps the wiring simple.

### HDX-57C (p1035): 1957 Chevy Car HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The triple-round '57 Chevy cluster holds six analog gauge readings and a big TFT display in this HDX system. You can check nearly any drivetrain reading without giving up that famous dash. Choose black or silver faces, then set separate lighting colors for the readings, needles and message centers.
>
> It installs in the cast-metal housing, which is required. The gauge pod and chrome inserts aren't included, so you'll use OEM or reproduction pieces. Reproduction chrome trim is sold separately. Add the matching HLC-57C clock for the passenger side. It only works with an HDX system. A metric version is a special order.
>
> Touch buttons in the face, or the Bluetooth app for Apple and Android, handle calibration and settings. A central control box pulls signals from the car's harness, so the install is much simpler.

### HDX-58C-IMP (p1094): 1958 Chevy Impala HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1958 Chevy, first of the X-frame cars, got an all-new dash, and this HDX system brings it up to current standards. Twin TFT message centers give full-color, real-time status for any drivetrain from a 283 to an LSA. Choose black or silver alloy faces.
>
> You'll need your stock instrument housing and front bezel trim. The bezel isn't included. A matching HLC clock is sold separately. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. A central control box connects the included solid-state senders.

### HDX-58C-VET (p1080): 1958-62 Chevy Corvette HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The one-of-a-kind 1958-62 Corvette dash gets twin TFT message centers with this direct-fit HDX package. Chrome bezels are included, and you choose black or silver alloy faces.
>
> You reuse your painted, cast dash housing, which isn't included. It connects to nearly any engine and transmission combination. The matching HLC-58C-VET clock, sold separately, fits the factory clock housing and plugs into the HDX control box. It can't be used alone. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness and connects the included solid-state senders.

### HDX-59C-IMP (p1068): 1959-60 Chevy Impala/ El Camino HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Whatever your 1959-60 Chevy cast pods ended up in, this HDX package installs directly into the stock housings. You get six analog sweep readouts and a large, full-color TFT message center. Choose black or silver alloy faces and your own lighting colors.
>
> It fits the 1959-60 Impala and El Camino. The bezel isn't included, so use an OEM or reproduction one. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Indicators stay hidden until they light, and every gauge has its own red warning light you can set. A central control box pulls signals from the car's harness and connects the included solid-state senders.

### HDX-60C-PU (p1123): 1960-63 Chevy Pickup HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1960-63 Chevy pickups need their own cluster, and this direct-fit HDX kit is made for them. A large TFT message center sits between six analog readings, with black or silver alloy faces.
>
> It's a drop-in that uses the stock bezel or trim, which isn't included. It doesn't fit GMC trucks. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android, and choose your lighting colors. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-61C-IMP (p1069): 1961-62 Chevy Impala HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> There's no need to cut up a 1961-62 Impala dash for round gauges. This direct-fit HDX system keeps the 1960s style and adds twin TFT message centers, so the driver can see key information at any time. Faces come in black or silver alloy.
>
> New chrome housings and bezels for the round gauges are included, and you reuse the rectangular speedometer trim piece. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android, and choose separate lighting colors for the readings, needles and message centers. Each gauge gets its own red warning light you can set. A central control box connects the included solid-state senders.

### HDX-62T-FJ (p1062): 1962-84 Toyota FJ HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Made for the stock gauge bezel in 1962-84 Toyota FJ models, this HDX system drops right in. Analog needles on black or silver alloy faces sit with a TFT message center, and you pick separate lighting colors for the readings and needles.
>
> It works with nearly any drivetrain. The bezel isn't included, so use an OEM or reproduction one. A custom 4,000 rpm tach for diesels and metric units are available on request, so contact Dakota Digital about those.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. A central control box pulls signals from the vehicle harness and hooks up the included solid-state senders.

### HDX-63C-IMP (p1070): 1963-64 Chevy Impala HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> With six analog sweep needles and a fully configurable TFT message center, a 1963-64 Impala gets all its information at your fingertips. It's a simple bolt-in, and the faces come in black or silver alloy.
>
> It also fits the Biscayne and Bel Air. The bezel isn't included, so use an OEM or reproduction one. Cars with factory A/C need some changes to the ductwork on the stock gauge bezel. A metric version is a special order.
>
> Use the built-in touch buttons or a Bluetooth app on iPhone or Android to set it up and pick your lighting colors. Indicators stay hidden until they light. A central control box pulls signals from the car's harness and connects the included solid-state senders.

### HDX-64C-CVL (p1058): 1964-65 Chevy Chevelle/ Malibu/ El Camino HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Six sweeping analog gauges and two easy-to-see TFT message centers bring a 1964-65 Chevelle, Malibu or El Camino up to spec. This direct-fit HDX system comes with black or silver faces, and you pick separate lighting colors for the readings, needles and message centers.
>
> It attaches directly to a stock or reproduction bezel, sold separately. Reproduction bezels are listed with this kit for 1964 and 1965 cars, with or without A/C. A metric version is a special order.
>
> Set it up with the touch buttons or the Bluetooth app for iPhone and Android. Indicators stay hidden until they light, and every gauge has its own red warning light you can set. A central control box hooks up the included solid-state senders to keep installation simple.

### HDX-64C-PU (p1038): 1964-66 Chevy Pickup HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Finish off your 1964-66 C10 with six analog gauge sweeps and a large TFT display in the middle. It mixes classic looks with modern readouts, so you always know what's going on under the hood. Faces come in black or silver alloy, with lighting colors you choose.
>
> This one-piece system bolts to your stock or reproduction bezel with the supplied hardware. The bezel isn't included, and it doesn't fit GMC models. A metric version is a special order.
>
> Touch buttons on the face, or the Bluetooth app for iPhone and Android, handle setup. The needle hubs are black nickel-plated spun aluminum. A central control box pulls signals from the truck's harness and connects the included solid-state senders.

### HDX-64P-GTO (p1077): 1964-67 Pontiac GTO/ LeMans/ Tempest HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Two TFT message centers and six analog gauge sweeps fill the four openings of a 1964-67 Pontiac A-body dash, so you can view nearly any reading you want. Order black or silver alloy faces, and pick your own lighting colors.
>
> The fully machined housing attaches directly to the stock gauge bezel of the GTO, LeMans and Tempest, including the 1963 Tempest. The bezel, trim and fascia aren't included. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness and hooks up the included solid-state senders to keep installation simple.

### HDX-65F-MUS (p1065): 1965-66 Ford Mustang HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A 1965-66 Mustang gets six analog gauge sweeps and a full-color TFT message center that fit right in. Choose black or silver faces to match your interior, along with your own lighting colors for the readings and needles.
>
> It's a direct fit for original and reproduction bezels, which are sold separately. Hooking it up to your drivetrain is easy, whether it's a 289 or a 5.0L Coyote. A metric version is a special order.
>
> Use the built-in touch buttons or a Bluetooth app on iPhone or Android for setup. Indicators stay hidden until they light, and every gauge has its own red warning light you can set. A central control box hooks up the included solid-state senders to keep installation simple.

### HDX-66C-CVL (p1056): 1966-67 Chevy Chevelle/El Camino HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Most aftermarket gauges won't fit the long, narrow instrument housing of a 1966-67 Chevelle, Malibu or El Camino, but this direct-fit HDX system does. Six analog gauge sweeps sit beside a large, full-color TFT message center, so the dash looks modern without looking out of place.
>
> Faces come in black or silver alloy. It uses your OEM or reproduction bezel, which isn't included, and a replacement bezel is listed with this kit. A metric version is a special order.
>
> Set it up with the touch buttons or the Bluetooth app for iPhone and Android, and choose separate lighting colors for the readings, needles and message center. Indicators stay hidden until they light. A central control box hooks up the included solid-state senders to keep installation simple.

### HDX-66C-NOV (p1072): 1966-67 Chevy Nova HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A single full-color TFT message center sits in the middle of this 1966-67 Nova cluster, with backlit analog needles on both sides. It all lives in a CNC machined housing. Choose black or silver alloy faces.
>
> The housing attaches to a stock or reproduction bezel, sold separately, the same way the factory cluster did. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android, and pick separate lighting colors for the readings and needles. Each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness and connects the included solid-state senders.

### HDX-66F-BRO (p1064): 1961-66 Ford Pickup HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Here's an all-in-one analog system with a large TFT message center, made to fit the stock dash of a 1961-66 Ford pickup. Choose black or silver alloy faces and set separate lighting colors for the readings and needles.
>
> It uses your existing bezel, which isn't included, and it doesn't fit Custom Cab models. It connects to just about any drivetrain combination. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-66F-BRO (p1061): 1966-77 Ford Bronco HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The early Bronco's flat dash has one round instrument on the left, and this bolt-in HDX system makes the most of it. Six analog instruments sit with a 2.4 inch full-color TFT message center, and the stock trim ring stays. Faces come in black or silver alloy.
>
> The bezel isn't included, so use an OEM or reproduction one. Tying it into the drivetrain of your choice is easy. A metric version is a special order.
>
> Calibrate it with the built-in touch buttons or a Bluetooth app on iPhone or Android, and choose separate lighting colors for the readings and needles. Every gauge has its own red warning light you can set. A central control box connects the included solid-state senders.

### HDX-67C-CAC (p1111): 1967 Camaro with Console gauges HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Chevy added the triple-round console gauges for high-powered first-year Camaros, and this HDX kit fills them. It brings two TFT message centers plus an analog clock. Choose black or silver alloy faces.
>
> It fits directly into your stock dash and console instrument housings. The dash and console bezels aren't supplied. It's a complete package and can't be split up. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-67C-PU (p1039): 1967-72 Chevy/ GMC Pickup HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Every opening in the original seven-hole '67-72 GM pickup cluster gets put to work. Six analog gauges and a clock fill the holes, and twin TFT message centers give you trip meters, miles to empty and 0-60 times. You pick black or silver alloy faces and your own lighting colors.
>
> It fits your stock or reproduction dash bezel, which is sold separately. A replacement bezel for these trucks is listed with this kit. A metric version in km/h and Celsius is a special order.
>
> Touch buttons on the face, or the Bluetooth app for iPhone and Android, handle setup. The needle hubs are spun aluminum, black nickel-plated to match the buttons. Each gauge has its own red warning light you can set. A central control box pulls signals from the truck's harness and connects the included solid-state senders, so the install stays simple.

### HDX-67F-MUS (p1066): 1967-68 Ford Mustang HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Five analog gauges and twin TFT message centers bolt straight into a 1967-68 Mustang bezel with this HDX system. Faces come in black or silver alloy, and you pick separate lighting colors for the readings, needles and message centers.
>
> It fits a stock or reproduction 1967-68 Mustang bezel, which isn't included. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor replaces a Ford or GM style cable. Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Every gauge has its own red warning light you can set. A central control box connects the included senders, which keeps installation simple.

### HDX-68C-CAC (p1082): 1968 Camaro with Console gauges HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Those four little gauges in the center console tell people your '68 Camaro means business. This bolt-in HDX system adds six analog readings plus twin TFT message centers, so you can see every vital at a glance without disturbing the rare factory housings. Faces come in black or silver alloy.
>
> It's a complete package and can't be split up. The dash and console bezels aren't supplied, so use OEM or reproduction ones. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness and connects the included solid-state senders.

### HDX-68C-CVL (p1060): 1968 Chevy Chevelle/ El Camino HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Those two large squares in the 1968 Chevelle, Malibu and El Camino dash have long been a puzzle. This HDX system bolts in and fills them with six analog gauge readings and a pair of TFT message centers. Pick black or silver alloy faces and your own lighting colors.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Indicators stay hidden until they light, and each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness and hooks up the included solid-state senders to keep installation simple.

### HDX-68C-VET (p1095): 1968-77 Chevy Corvette HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Build your 1968-77 Mako Shark Vette right without cutting hard-to-find dash parts for universal gauges. The speed and tach, with full-color TFT message displays, sit front and center. The satellites and an analog clock live in the center console panel.
>
> The supplied sensors work with nearly any engine, stock, modified or late model. Choose black or silver alloy faces. The bezel isn't included. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-69C-CVL (p1059): 1969 Chevy Chevelle/ Malibu/ El Camino HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1969 Chevelle had a one-year-only dash, and this HDX kit is made for it. Each large opening gets three analog needles and a full-color TFT message center, with an analog clock between them. Pick black or silver faces.
>
> It drops straight into the original or reproduction instrument housing of a 1969 Chevelle, Malibu or El Camino. The bezel isn't included, so use an OEM or reproduction one. A metric version is a special order.
>
> Use the touch buttons or the Bluetooth app for iPhone and Android to set it up and choose your lighting colors. Each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness and connects the included solid-state senders.

### HDX-69F-MUS (p1067): 1969-70 Ford Mustang HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Two full-color TFT message centers show a wealth of information in this drop-in HDX system for the 1969-70 Mustang. Analog needles sit on black or silver alloy faces, with lighting colors you choose.
>
> It uses your stock instrument housing and bezel, and new clear lenses are included. The bezel itself isn't included. Add the matching clock for the passenger side, sold separately. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Indicators stay hidden until they light, and each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness and connects the included solid-state senders.

### HDX-70C-CVL (p1054): 1970-72 Chevy Chevelle SS/Monte Carlo/El Camino & 71 GMC Sprint SP HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Upgrade a 1970-72 Chevelle or El Camino with the SS-style dash to six analog gauge sweeps and a pair of TFT message centers. Faces come in black or silver alloy. The original turn signal, high beam and brake indicator spots are updated with LEDs.
>
> It screws directly into an original or aftermarket gauge carrier, sold separately, and a 1970-72 Chevelle SS carrier is listed with this kit. The bezel isn't included, so use an OEM or reproduction one. It also fits the Monte Carlo and the 1971 GMC Sprint SP. A metric version is a special order.
>
> Use the touch buttons or the Bluetooth app for iPhone and Android to set lighting colors and calibrate. Each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness and connects the included solid-state senders.

### HDX-70C-MAL (p1085): 1970-72 Chevy Malibu/ non SS Chevelle/ El Camino HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Does your 1970-72 Malibu or El Camino have the sweep-style cluster? This drop-in HDX system gives you six analog instruments and a large TFT message center for extra readings. Pick black or silver alloy faces.
>
> A new front lens and rear housing come with it, and the original indicator strip goes away. The bezel isn't included, so use an OEM or reproduction one. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android, and choose your lighting colors. Each gauge gets its own red warning light you can set. A central control box connects the included solid-state senders.

### HDX-70P-FIR (p1180): 1970-81 Pontiac Firebird HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Your disco-era Pontiac gets modern features with this drop-in HDX system. Matte-black machined aluminum gauge bezels suit the existing dash panel, and twin TFT message displays come standard. Choose black or silver alloy faces.
>
> The kit has five gauges. In a three-gauge dash, you can leave out the oil and temp gauges and still see that data in the message centers. The bezel, fascia and dashboard aren't included. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-71C-CAP (p1084): 1971-76 Chevy Caprice/ Impala HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Designed as a drop-in for the 1971-76 Chevy Impala and Caprice, this HDX system includes the sending units it needs. A large TFT message center lets you customize extra readings, and you set the lighting colors to match any paint scheme.
>
> Choose black or silver alloy faces when you order. The bezel isn't included, so use an OEM or reproduction one. A metric version is a special order.
>
> Calibrate it with the built-in touch buttons or the Bluetooth app for Apple and Android. The needle hubs are black nickel-plated spun aluminum, indicators stay hidden until they light, and each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness.

### HDX-73C-PU (p1040): 1973-87 Chevy Pickup, 1973-91 Chevy Blazer, GMC Jimmy and Suburbans HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A big speedometer and tach sit front and center in the 1973-87 Chevy and GMC pickup cluster, with the smaller gauges off to the side. This HDX system adds a TFT display in each large opening, so you can view any readings you like. Faces come in black or silver alloy, with separate lighting colors you pick.
>
> It also fits 1973-91 Chevy Blazer, GMC Jimmy and Suburban, plus heavy duty pickups. The bezel isn't included, so use an OEM or reproduction one. A metric version is a special order.
>
> The built-in buttons make calibration easy, or use the Bluetooth app for iPhone and Android. Each gauge has its own red warning light you can set. A central control box pulls signals from the truck's harness and connects the included solid-state senders.

### HDX-77C-CAP (p1182): 1977-90 Chevy Caprice/ Impala & 1984-86 Pontiac Parisienne HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Get your box Chevy looking right with this bolt-in HDX system. No cutting is needed for color-changing backlighting, full-color digital screens and mobile app control, though a bit of wiring finishes the conversion.
>
> It fits 1977-90 Chevy B-bodies and the 1984-86 Pontiac Parisienne, with a stock drivetrain or an LS swap. The bezel isn't included. Pick black or silver alloy faces. A metric version is a special order.
>
> Calibrate it with the built-in touch buttons or the Bluetooth app for Apple and Android. The needle hubs are black nickel-plated spun aluminum, and each gauge gets its own red warning light you can set. A central control box connects the supplied solid-state senders.

### HDX-78C-MC (p1055): 1978-88 Chevy Monte Carlo, 1978-87 Chevy El Camino/ Malibu/ Caballero HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> G-body owners with the six-round gauge cluster get six analog readings and a pair of TFT message centers with this HDX system. The turn signals stay in their stock locations. Faces come in black or silver alloy, with lighting colors you choose.
>
> It fits the 1978-88 Monte Carlo and 1978-87 El Camino, Malibu and Caballero with the six-round cluster. It won't fit the rectangular sweep-style speedometer cluster. Use your stock housing, blackout plate and front bezel for an easy upgrade. The bezel isn't included. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. A central control box pulls signals from the car's harness and connects the included solid-state senders.

### HDX-78C-VET (p1096): 1978-82 Chevy Corvette HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A 1978-82 Corvette is a great starting point, and this bolt-in HDX system brings its cockpit-style interior up to date. A pair of TFT message centers shows the data you need in full color. Choose black or silver alloy faces.
>
> The whole system installs into your stock instrument bezels and housings. The bezel isn't included. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android, and pick your lighting colors. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-78o-CUT (p1197): 1978-88 Oldsmobile Cutlass HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Rectangle or round-gauge cluster, this direct-fit HDX system works in your 1978-88 Cutlass. A full-color TFT message center shows the data you choose, and six analog gauges give you information at a glance.
>
> It needs your stock cluster and bezel, which aren't included. To buy this kit, call 1-800-593-4160 or contact a dealer. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android, and pick your lighting colors. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-84B-REG (p1190): 1984-87 Buick Regal and Grand National HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Regals, T-Types and Grand Nationals can run this direct-fit HDX system, with six analog instruments around a full-color TFT message center. Set the display to show what you need, like boost, transmission temperature or fuel pressure.
>
> It fits the stock 1984-87 Regal cluster and housing. On a Grand National, boost shows in the message centers, and a Grand National version with the SEN-09-7 is listed. Thirty LED lighting colors match your paint and interior. Metric versions are a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and a central control box keeps the wiring simple.

### HDX-87F-MUS (p1315): 1987-89 Ford Mustang HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A 1987-89 Fox Body Mustang gets six analog instruments and a large, full-color TFT message center you can program, all in the stock cluster and housing. There are 30 LED backlighting colors to choose from.
>
> Faces come in black or silver alloy. The bezel isn't included, so use an OEM or reproduction one. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables.

### HDX-90F-MUS (p1317): 1990-93 Ford Mustang HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Late Fox Body Mustangs from 1990-93 get six analog instruments and a large, programmable TFT message center, all fitting the stock cluster and housing. Pick from 30 LED backlighting colors.
>
> Faces come in black or silver alloy. The bezel isn't included, so use an OEM or reproduction one. A metric version is a special order.
>
> Use the built-in touch buttons or a Bluetooth app on iPhone or Android for setup. Indicators stay hidden until they light. Water temperature, oil pressure and speed sensors are included, each with a 10 ft harness, and the speed sensor works with Ford or GM style cables. A central control box keeps the wiring simple.

### HDX-95C-PU (p1339): 1995-98 Full-size, 1995-00 SUV & HD Pickup Chevy/ GMC HDX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> This direct bolt-in, six-gauge HDX system fits 1995-98 GM trucks and 1995-2000 SUV and HD models. It adds modern features and works with any engine and transmission, all inside the OEM dash housing.
>
> It isn't a plug-in install. The included sensors get wired into the OEM harness. The bezel isn't included, so use an OEM or reproduction one. Faces come in black or silver alloy. A metric version is a special order.
>
> Set it up with the built-in touch buttons or a Bluetooth app on iPhone or Android. Each gauge gets its own red warning light you can set. Each sensor has a 10 ft harness, and a central control box keeps the wiring simple.

### HDX-96J-TJ (p1333): 1996-03 Jeep TJ and 1997-01 Jeep Cherokee XJ HDX Instrument System

**What was wrong:** wording carried over from the original copy (12+ word run).

> Sky-high lifts or V8 LS power, a 1996-03 Jeep TJ can take nearly anything, but the stock gauges can't keep up. This drop-in HDX package bolts directly into the OEM dash framework and works with whatever upgrades you add.
>
> Pick black or silver alloy faces and separate lighting colors for the readings, needles and message centers. A metric version is a special order.
>
> Calibrate it with the built-in touch buttons or the Bluetooth app for Apple and Android. The needle hubs are black nickel-plated spun aluminum, indicators stay hidden until they light, and each gauge gets its own red warning light you can set. A central control box connects the supplied solid-state senders.

### RTX-32F-X (p1210): 1932 Ford Car RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Your deuce gets a factory-styled cluster with a full-color TFT display built in. The speedometer and fuel gauge are analog, while the tach, oil pressure and water temp show as LED bar graphs. Voltage reads in the message center. It looks like original equipment until the LED backlighting comes on in your color scheme.
>
> It's a direct fit for the 1932 Ford car, and the machined aluminum bezel fits the stock dash. It measures 12.135 by 4.925 inches overall and needs an 11.836 by 4.626 inch cutout. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-33F-X (p1240): 1933-34 Ford Car RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Part jewelry, part car part: brushed faces sit in a chrome bezel with an engine-turned aluminum insert. An LED bar-graph tach wraps around the outside of the speedometer, and a full-color TFT message center shows more than the standard six readings.
>
> The billet aluminum housing matches the raised stamped section of a 1933-34 Ford car dash. Cutting is required to install it. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-40F-X (p1203): 1940 Ford Car and 1940-47 Ford Truck RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1940 Ford dash is an icon in street rods, and this RTX kit keeps its OEM style. A feature-rich TFT message center sits inside the factory-look layout. A casual glance says original equipment, until the LED backlighting comes on in your color scheme.
>
> It fits the stock dash opening in 1940 Ford cars and 1940-47 Ford pickups. A chrome-plated, machined bezel comes with the kit. A matching clock is sold separately. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors are included with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-42F-X (p1307): 1942-48 Ford Car RTX Instrument System

**What was wrong:** wording carried over from the original copy (12+ word run).

> Add a touch of elegance to a WWII-era Ford or Mercury car. These RTX gauges are styled after the originals and filled with modern technology, so you keep the OEM design you love and gain modern accuracy. A bar-graph tach rides with the speedometer, oil, water, fuel and volts.
>
> The '42-48 face colors shift the color-selectable backlighting a bit. That trims the 31 color choices, and pure white looks like a warm incandescent. A matching RLC clock is sold separately. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-47C-PU-X (p1149): 1947-53 Chevy/ GMC Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Chrome-plated billet aluminum bezels give this dual-round 1947-53 Chevy and GMC pickup cluster a decidedly stock look. The 120 mph speedometer is styled like the original, and a bar-style tachometer sits inside its sweep. A single TFT message center brings up extra data when you want more, and the LED backlighting comes on in your colors.
>
> The machined aluminum and chrome bezels are included. Oil pressure, water temp, fuel and volts round out the readings. Water temperature, oil pressure and speed sensors come in the box, each with a 10 ft harness. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. A two-sided rocker switch handles setup, and one central control box keeps the install simple.

### RTX-49C-X (p1286): 1949-50 Chevy Car RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Designed for the 1949-50 Chevy dash, this RTX system drops right into place in a billet aluminum gauge housing. The faces carry over the original instrument style, and inside are LED backlighting, stepper motor needle movements and a full-color TFT message center.
>
> It bolts in with stock hardware and keeps the OEM crimp-on front bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-49F-X (p1283): 1949-50 Ford Car RTX Instrument System

**What was wrong:** wording carried over from the original copy (12+ word run).

> It looks stock, but this direct-fit RTX system for the 1949-50 Ford car marries the original gauge design with a full-color TFT message center and LED backlighting. A spun aluminum housing holds it all together, and it talks to nearly any drivetrain.
>
> A chrome-plated billet aluminum bezel comes with it. A matching RLC clock is sold separately. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-50M-X (p1321): 1950-51 Mercury RTX Instrument System

**What was wrong:** wording carried over from the original copy (12+ word run).

> Separate round gauges don't do justice to the 1950-51 Mercury dash. This RTX system pays tribute to Mercury styling and adds features you only get with modern technology, including an analog clock.
>
> The factory AM radio is eliminated to make room for the instruments. It uses your OEM bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-51C-X (p1273): 1951-52 Chevy Car RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Following the dash contour of a 1951-52 Chevy car, chrome-plated billet aluminum bezels frame faces that carry over the original instrument style. Inside you get LED backlighting, stepper motor needle movements and a full-color TFT message center. A ring of LEDs around the speedometer scale shows rpm.
>
> It bolts into the stock gauge openings with stock hardware. A matching RLC clock is sold separately. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-51F-X (p1287): 1951 Ford Car RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Give the stock, body-colored instrument bezel in your 1951 Ford car a facelift. This bolt-in RTX kit is all new from the lens back but keeps the stock appearance, with a full-color TFT message center at the bottom and a bar-graph tach alongside the speedometer.
>
> It uses your OEM bezel, which isn't included. A matching RLC clock is sold separately. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-53C-VET-X (p1337): 1953-57 Chevy Corvette RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Machined chrome gauge housings drop straight into the stock openings of a 1953-57 Corvette. This bolt-in, 7-gauge RTX system, clock included, keeps the cool features of the OEM design and adds a full-color TFT message center, LED indicators, precision stepper motor needles and EFI integration.
>
> The chrome bezel is included, and the system fits the OEM dashboard. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-53C-X (p1274): 1953-54 Chevy Car RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Keep your stock instrument bezel and the OEM look of a 1953-54 Chevy car, and add LED backlighting in colors you set, a full-color TFT message center and late-model drivetrain hookup.
>
> A small section of the dash between the speedometer and clock has to be trimmed. The bezel isn't included, so use an OEM or reproduction one. The system takes the place of the stock automatic gear indicator above the column, so add the GSS-3000 (sold separately) to show gear position. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup.

### RTX-53F-PU-X (p1250): 1953-55 Ford Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1953-55 Ford F100 cluster keeps its original look and style in this RTX system, with modern features added inside. A large, full-color TFT message center and precision needle movements do the work, and a bar-graph tach rides along with the speedometer, oil, water, fuel and volt readings.
>
> It fits the original dashboard. A chrome-plated billet aluminum bezel and a new lens are included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-54C-PU-X (p1231): 1954 Chevy Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Two round gauges with chrome-plated billet aluminum bezels give a 1954 Chevy pickup a stock look. Inside the sweep of the OEM-styled 120 mph speedometer is a bar-type tachometer, so the vintage feel stays while the system does it all. A single TFT message center brings up extra data when you want it.
>
> The machined aluminum and chrome bezel is included. Oil pressure, water temp, fuel and volts round out the readings. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and the LED backlighting comes on in the colors you choose.

### RTX-55-GMC-X (p1402): 1955-59 GMC Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> GMC owners asked, and here's the RTX gauge system for the stock dash panel of a 1955-59 GMC truck. It was engineered from a stock GMC dash and uses the stock mounting points, so the panel needs no modification.
>
> New CNC machined, chrome-plated aluminum gauge trim rings are included. The bezel and fascia aren't, so use OEM or reproduction ones. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-55C-PU-X (p1135): 1955-59 Chevy Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> It looks like a stock take-out cluster from a 1955-59 Chevy pickup, but it's all new and fully electronic. A tachometer now matches the small gauges up top, and the speedometer reads to 120 mph. A single TFT message center is set into a mesh pattern behind the speedometer needle, and the LED backlighting comes on in your colors with the key.
>
> It fits your stock or reproduction chrome bezel, which is sold separately. It doesn't fit GMC trucks. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come in the box, and one central control box keeps setup simple.

### RTX-55C-X (p1134): 1955-56 Chevy Car RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Even the mesh pattern behind the speedometer needle matches the stock 1955-56 Chevy cluster. Most people will take it for factory until you turn the key. Then the LED backlighting comes on in the colors you pick, and a full-color TFT message center shows trip meters, miles to empty and 0-60 times.
>
> You'll use your stock or reproduction bezel, which isn't included. The system takes the place of the stock automatic gear indicator above the steering column, so add the GSS-3000 sensor (sold separately) if you want gear position on the screen. The matching RLC-55C clock finishes off the passenger side. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. One central control box keeps installation and setup simple.

### RTX-56F-PU-X (p1251): 1956 Ford Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> You don't have to choose between the arch-shaped speedometer of a '56 F100 and modern gauges anymore. This RTX system keeps the large, sweeping speedometer look and adds a full-color TFT message center that can show extra readings. A bar-graph tach joins the oil, water, fuel and volt gauges.
>
> It's a bolt-in kit that uses your OEM bezel, which isn't included. No drilling holes for round gauges. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-57C-X (p1136): 1957 Chevy Car RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Only three gauges show on this stock-looking '57 Chevy cluster, but there are six readings inside. The tach, oil pressure and voltage are hidden LED bars that only appear when the key is on. A large TFT message center sits front and center, while the rest of the cluster looks straight out of 1957.
>
> It fits into your original cast housing. The gauge pod and chrome inserts aren't included, so you'll use OEM or reproduction parts. Replacement chrome inserts and the matching RLC-57C clock are sold separately. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. One central control box keeps installation and setup simple, and the LED backlighting comes on in the colors you choose.

### RTX-57F-PU-X (p1434): 1957-60 Ford Pickup & 1961-67 Econoline Van RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Ford fans call the 1957-60 F-Series the "Effie," and its wider, lower look was a big change for Ford trucks. This RTX system updates that dash with analog speed, oil pressure, water temp, fuel and volts, plus an LED bar-graph tach.
>
> It uses your OEM bezel, which isn't included. The title also lists the 1961-67 Econoline van. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. The speed sensor works with Ford or GM style cables and needs about 5 inches of clearance. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-58C-IMP-X (p1290): 1958 Chevy Impala RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1958 Chevy full-size dash is defined by its long, sweeping speedometer, and this RTX cluster recreates it. Hidden tach, voltage and oil pressure gauges sit just under the speedometer sweep, and full-color TFT message centers sit just inside the OEM-style turn signals at each end.
>
> You'll need your stock instrument housing and front bezel trim. The bezel isn't included. A matching RLC clock is sold separately. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-58C-VET-X (p1275): 1958-62 Chevy Corvette RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Love the stock 1958-62 Corvette interior but want better accuracy and visibility? This bolt-in RTX system keeps the cool features of the OEM design and adds a full-color TFT message center, LED indicators, precision stepper motor needles and EFI integration.
>
> Chrome-plated billet gauge bezels are included. It needs the stock cast-metal dash pods, and the dash housing isn't included. A matching RLC clock is sold separately. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-59C-CAD-X (p1375): 1959 Cadillac RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Billboard tail fins and acres of chrome make the 1959 Cadillac impossible to mistake. This RTX system respects the OEM gauge cluster layout and adds every modern update, with a bar-graph tach and the clock included.
>
> It connects simply to OEM or aftermarket engines. The bezel isn't included, so use an OEM or reproduction one. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup.

### RTX-59C-IMP-X (p1189): 1959-60 Chevy Impala/ El Camino RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The five-pod 1959-60 Chevy dash has become an icon, showing up in everything from kustoms to mini trucks. This RTX system keeps factory-styled faces and adds a large, full-color TFT display. You choose your own lighting colors, and a bar-graph tachometer joins the speedometer, oil, water, fuel and volt readings.
>
> It fits the 1959-60 Impala and El Camino. You'll need the stock gauge pods, which Dakota Digital doesn't sell, and your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. One central control box keeps installation and setup simple.

### RTX-60C-CAD-X (p1355): 1960 Cadillac RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Big rounded panels and mile-long fins made the 1960 Cadillac a classic, and its interior got the look just right. This RTX system honors the OEM gauge layout, analog clock included, and adds every modern update you can think of.
>
> It connects simply to OEM or aftermarket engines. It uses an OEM or reproduction style bezel. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-60C-PU-X (p1185): 1960-63 Chevy Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Keep the vintage look of your 1960-63 Chevy C10 and get modern readouts. A bar-graph tachometer is tucked under the 120 mph speedometer, the turn signals keep their factory style, and a full-color TFT message center sits in the middle. The LED backlighting comes on in your colors when you turn the key.
>
> Drop it into a stock or reproduction bezel, which isn't included. It doesn't fit GMC. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-61C-IMP-X (p1198): 1961-62 Chevy Impala RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> This RTX system follows the shapes of the 1961-62 Chevy dash and drops right in. It keeps the stock look, then lights up in multiple colors with the key on. Behind the faces are a speedometer, tach, oil pressure, water temp, fuel and volt readings, plus a TFT message center.
>
> New aluminum chrome bezels come with it for the round gauges, and your stock stamped speedometer trim gets reused. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps the install simple.

### RTX-61L-X (p1381): 1961-63 Lincoln RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> New aluminum bezels dripping with chrome surround OE-inspired RTX faces in this system for the 1961-63 Lincoln. It's a fit for the stock three-piece dash assembly, with a bar-graph tach alongside the speedometer, oil, water, fuel and volts.
>
> The new chromed aluminum bezels are included. The stock housings and mounting plate aren't. Installation requires a permanent change inside the stock cluster to make room, so check the installation manual first. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-62T-FJ-X (p1184): 1962-84 Toyota FJ RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Your 1962-84 Toyota FJ40 keeps its vintage look with this RTX cluster. A full-color TFT message center sits in the center of the speedometer, and an LED bar-graph tach curves around its outer edge. It's modern tech that looks like stock equipment.
>
> A new machined aluminum bezel in matte silver powdercoat replaces the stamped original, and it's included. The whole assembly drops in where your stock FJ dash panel goes. The metric version costs nothing extra but is a special order. Diesel interface parts are also available.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. One central control box keeps installation and setup simple.

### RTX-63C-IMP-X (p1199): 1963-64 Chevy Impala RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Looks like 1963, works like today. This RTX system is drawn from the factory cluster in the 1963-64 Chevy Impala, Bel Air and Biscayne, then adds LED backlighting, TFT message centers and full color-changing lighting. Pick the 1963 or 1964 style.
>
> Use your stock steel front bezel, which isn't supplied. Cars with factory A/C need some changes to the ductwork on the stock gauge bezel. It connects to anything from a 283 to a twin turbo LS3. A metric version of each style is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-63C-NOV-X (p1234): 1963-65 Chevy Nova RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Skip cutting the dash in your 1962-65 Chevy II or Nova. This direct-fit RTX system is designed to mimic the factory cluster, with a TFT message center and fully working gauges for oil pressure, coolant temperature, fuel level and voltage. The turn signals keep their factory locations, now lit by LEDs.
>
> It uses a stock or reproduction 1963-65 gauge bezel, which isn't included, so a 1962 car needs the later bezel. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-63C-VET-X (p1249): 1963-67 Chevy Corvette RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Pick the 1963, 1964 or 1965-67 style face to match your Corvette. Each one copies the stock layout well enough to pass for factory. Then you turn the key, and the LED backlighting lights up in your colors. TFT message centers show just about any reading you want.
>
> It uses your OEM or reproduction bezel, which isn't included. A matching RLC clock in each style is sold separately. A metric version of each style is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-64C-CVL-X (p1224): 1964-65 Chevy Chevelle/ Malibu/ El Camino RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Spun aluminum accents and a layered, multi-depth face finish off a 1964-65 Chevy A-body, from a pro-touring build to a near-stock restoration. Twin TFT message centers look right at home in the sixties design. New LEDs light the stock turn signal locations.
>
> It bolts in with your OEM or reproduction bezel, which isn't included. Choose your car's year and whether it has the A/C vent when you order. Reproduction bezels for 1964 and 1965 cars, with or without A/C, are listed with this kit. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-64C-PU-X (p1151): 1964-66 Chevy Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> No need to hunt for a factory tach cluster for your 1964-66 C10. This RTX system keeps the vintage look and puts an analog tachometer on the right. A 2.4 inch TFT message center on the left shows just about any extra reading you want, and a small center display has a simulated tumbler odometer.
>
> It needs a stock or reproduction bezel to install, which isn't supplied. It doesn't fit GMC. A metric version is a special order.
>
> The housing is CNC machined, with electronics Dakota Digital designs and builds in-house. You set it up with the included rocker switch, and the LED backlighting comes on in the colors you choose. One central control box keeps installation simple.

### RTX-64F-FAL-X (p1272): 1964-65 Ford Falcon, Ranchero and Mustang RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The unique cluster in a 1964-65 Falcon or non-Pony Mustang gets a direct-fit RTX upgrade with an OEM look. A hidden LED bar-graph tach sits above the wide speedometer sweep, and twin full-color TFT message centers flank it.
>
> It uses the stock front bezel, OEM or reproduction, which isn't included. It also fits the Ranchero. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-64P-GTO-X (p1237): 1964-67 Pontiac GTO/ LeMans/ Tempest RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> One Pontiac cluster fits the 1964-67 GTO, Tempest and Le Mans, and so does this RTX system. Twin TFT message centers and LED backlighting keep you informed, while the original styling cues stay intact. Even a straight restoration can run it.
>
> A machined aluminum housing gives an accurate fit. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-65C-CAD-X (p1380): 1965-66 Cadillac RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Cruise a 1965-66 Cadillac and the dash lights up with a full six-gauge RTX display, plus a matching clock in the stock location. A bar-graph tach rides with the speedometer, oil, water, fuel and volt gauges.
>
> It uses an OEM or reproduction style bezel. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-65C-IMP-X (p1383): 1965 Chevy Caprice/ Impala RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Chevy's 1965 full-size cars got bigger and better, and so does this direct-fit RTX system for the Impala, Caprice, Bel Air and Biscayne. It keeps the factory look until the key turns and the LED backlighting comes on in your colors.
>
> TFT message centers show just about any reading you want. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup.

### RTX-65F-MUS-X (p1209): 1965-66 Ford Mustang RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Even purists will have a hard time spotting this upgrade in a 1965-66 Mustang. It keeps every factory design element and adds a full-color TFT message center. A hidden LED bar-graph tachometer runs around the outside of the speedometer sweep, and the LED backlighting comes on in your colors.
>
> It's designed for the GT and Pony interiors of 1965 and all 1966 Mustangs. Bolt it into your stock or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-65F-PU-X (p1421): 1965-66 Ford Custom Cab Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Chrome accents and nicer trim set the 1965-66 Ford Custom Cab apart, and collectors still hunt for them. This direct-fit RTX system shows speed, water temp and fuel as analog gauges, while the tach, oil pressure and volts read as LED bar graphs.
>
> It uses your OEM bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. It needs about 5 inches of clearance. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-66C-CVL-X (p1152): 1966-67 Chevy Chevelle/ El Camino RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A long, sweeping speedometer flanked by dual gauges keeps the factory feel of a 1966-67 Chevelle, Malibu or El Camino. Turn the key and two 1.8 inch TFT message centers, LED backlighting and hidden indicators come alive. An LED bar-graph tach sits just below the speedometer, invisible until the key is on, and the horizontal lines on the face stay for a stock look.
>
> It uses your OEM or reproduction bezel, which isn't included. A reproduction bezel for the 1966-67 Chevelle is listed with this kit. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-66C-IMP-X (p1384): 1966 Chevy Caprice/Impala RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> From a base Biscayne to a loaded Caprice, and from a 250 six to a 427 or a late-model engine, this direct-fit RTX system suits any 1966 Chevy full-size car. A bar-graph tach joins the speedometer, oil, water, fuel and volt gauges.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-66C-NOV-X (p1235): 1966-67 Chevy Nova RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Showroom stock is how this 1966-67 Nova dash looks with the key off. Admirers have to look twice to spot the full-color TFT message centers and the LED bar graphs for oil pressure and volts. With it on, the driver gets clear readings for speed, rpm, water temp and fuel too.
>
> It's a direct fit for your stock 1966-67 Nova gauge bezel, OEM or reproduction, which isn't included. Drag racers, autocross fans and street machiners all use it. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-66F-BRO-X (p1187): 1961-66 Ford Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> People will look twice at the dash of your 1961-66 F100. This factory look-alike keeps the vintage style, adds a tachometer and puts a large, full-color TFT message center in the middle that shows the readings you choose. Orange needles and spun-aluminum accents on the face finish the look, and the LED backlighting comes on in your color scheme.
>
> It fits your existing bezel and needs a stock steel bezel, which isn't included. It doesn't fit Custom Cab models. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-66F-BRO-X (p1175): 1966-77 Ford Bronco RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Orange needles and spun-aluminum accents on the face give this 1966-77 Bronco cluster a factory look, and it adds a tachometer. A large, full-color TFT message center shows the readings you choose. A casual glance says original equipment, until the LED backlighting comes on in your color scheme.
>
> It fits your stock steel instrument bezel, which isn't included. It also fits 1961-66 Ford pickups with the stock bezel, except Custom Cab. A metric version in km/h and Celsius is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-67C-CAC-X (p1256): 1967 Camaro with Console gauges RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The one-year-only 1967 Camaro console gauge layout finally gets accuracy to match its looks. This RTX package takes the place of the original instruments, adds twin TFT message centers and even recreates the analog clock.
>
> It uses the stock bezels and gauge housings from your '67 Camaro. The dash and console bezels aren't supplied. It's a complete package and can't be split up. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-67C-CAM-X (p1154): 1967-68 Camaro/ Firebird RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> At first look it's a simple speedometer and tach combo, styled after the stock 1967 or 1968 Camaro cluster. Turn the key and four more readings appear as LED bars for oil pressure, coolant temperature, fuel and volts. Most people won't see them, but the driver has them front and center. Each pod also has a TFT message center for extra information.
>
> The 1967 and 1968 graphic styles differ, but both fit either year, so pick the period-correct look or the one you like. It fits directly into a stock or reproduction gauge bezel, sold separately, and a replacement bezel is listed with this kit. A metric version of each style is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-67C-IMP-X (p1385): 1967 Chevy Caprice/Impala RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Many critics call the 1967 Impala Chevy's best ever, and this direct-fit RTX system fits the dash of any full-size car in that year's lineup. An analog clock joins the speedometer, tach, oil, water, fuel and volt gauges.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-67F-MUS-X (p1217): 1967-68 Ford Mustang RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Showroom-fresh looks with modern features: this bolt-in RTX package for the 1967-68 Mustang keeps the factory style. Analog gauges cover speed, rpm, oil pressure, water temp and fuel. Twin TFT displays show system voltage and nearly any other reading you want.
>
> It works with a stock or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-67F-PU-X (p1260): 1967-72 Ford Pickup RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> An LED bar-graph tach above the speedometer and twin TFT message centers keep a 1967-72 Ford F-Series driver up to date in full color. With Bluetooth and the free mobile app, you can change the LED backlighting colors to suit your mood.
>
> This bolt-in upgrade uses your stock plastic or metal gauge bezel, which isn't included. Sensors for oil pressure, coolant temp and speed come in the kit. For a Lightning or Coyote drivetrain, the BIM-01-2 OBD-II/CAN interface makes hookup simple. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. One central control box keeps installation and setup simple.

### RTX-68C-CAC-X (p1257): 1968 Camaro with Console gauges RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> For a 1968 Camaro with the optional console gauges, this RTX system brings all-new instruments with 1968 styling. Large TFT message centers sit in the speedometer and tach, so you keep the vintage look and get modern functions and accuracy.
>
> The dash and console bezel aren't supplied, and the kit can't be split up. A replacement speedometer and tach bezel is listed with this kit. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-68C-CVL-X (p1226): 1968 Chevy Chevelle/ El Camino RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1968 Chevelle, Malibu and El Camino got two large square gauge openings with the new Coke-bottle body. This bolt-in RTX system keeps the OEM look and fills them with a full-color TFT message center under the speedometer and an 8,000 rpm tach in the center of a quad gauge.
>
> It uses your stock bezel, OEM or reproduction, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and the LED backlighting comes on in the colors you pick.

### RTX-68C-IMP-X (p1386): 1968 Chevy Caprice/Impala RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Chevy big-car fans get another option: a direct-fit RTX system for the 1968 Impala, Caprice, Bel Air and Biscayne. The speedometer, tach and clock are analog, and the oil, water, fuel and volt readings show as LED bar graphs.
>
> It uses your OEM bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and TFT message centers show extra readings.

### RTX-68C-VET-X (p1252): 1968-77 Chevy Corvette RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Early C3 Corvettes get a decidedly original look with twin TFT message centers inside. This bolt-in RTX system covers 1968-77 cars and includes the clock. When the key turns, the LED backlighting comes on in your colors.
>
> You reuse your stock rear instrument housings and front bezels, and new clear lenses come with the kit. The bezel isn't included. Mating it to a late-model drivetrain is simple. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. The TFT message centers can show just about any reading, and a single central control box makes installing and setup simple.

### RTX-69C-CAC-X (p1264): 1969 Camaro with Console gauges RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The optional console gauges are the icing on the cake of a '69 Camaro, and this RTX system replicates them. It adds LED backlighting, stepper motors for the needles and two large, full-color TFT message centers.
>
> The dash and console bezel aren't supplied, and the kit can't be split up. A 1969 Camaro instrument carrier is listed with this kit. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-69C-CVL-X (p1233): 1969 Chevy Chevelle/ El Camino RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Love the look of the 1969 Chevelle, Malibu and El Camino dash but want more than 1960s technology? This RTX system has a clock and tachometer, plus analog readings for oil pressure, temp, volts and fuel. LEDs light the factory turn signal locations.
>
> It bolts in using your stock dash bezel and components. The bezel isn't included, so use an OEM or reproduction one. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-69C-IMP-X (p1413): 1969-70 Chevy Caprice/ Impala RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Chevy called the 1969-70 Caprice and Impala luxury sedans, and others called them land yachts. This RTX system is the missing piece. Speed, water temp and fuel are analog, while the tach, oil pressure and volts show as LED bar graphs.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-69F-MUS-X (p1221): 1969-70 Ford Mustang RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Bolted behind the stock bezel of a '69-70 Mustang, this RTX system keeps the OEM styling and vintage feel. Full LED backlighting makes the gauges easy to see at night, and TFT message centers keep you informed of what's happening under the hood.
>
> It's a direct fit that uses your OEM or reproduction bezel, which isn't included. Add the matching RLC clock for the passenger side, sold separately. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-70C-CAM-X (p1156): 1970-78 Camaro RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Side by side with a stock 1970-78 Camaro cluster, you'd be hard pressed to tell them apart until the key turns. Then a pair of TFT displays come alive, and you can set them up however you choose. The LED backlighting comes on in your colors.
>
> It fits a stock or reproduction instrument bezel, which isn't included, and it also fits 1979-81 bezels. It doesn't fit the Firebird. Late-model drivetrains are straightforward to tie in. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps the install simple.

### RTX-70C-MAL-X (p1213): 1970-72 Chevy Malibu/ non SS Chevelle/ El Camino RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Think twice before swapping out the sweep-style dash in your 1970-72 Malibu, non-SS Chevelle or El Camino for an SS conversion. This bolt-in RTX system adds a tach on the right, with fuel and temp gauges beside the speedometer. A pair of TFT displays sits under the speedometer and shows oil pressure and volts, so the original look stays and nothing is missing.
>
> The fully machined aluminum housing is powdercoated black. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-70P-FIR-X (p1280): 1970-81 Pontiac Firebird RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The dash is part of why the second-gen Firebird has a cult following, and this direct-fit RTX package keeps its original styling. Matte black machined aluminum bezels hold full-color TFT message centers and precision stepper motor gauges, plus an analog clock.
>
> The kit has five gauges. In a three-gauge dash, you can leave out the oil and temp gauges and still see that data in the message centers. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-70o-CUT-X (p1374): 1970-72 Oldsmobile Cutlass 442 RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The three round gauges of a 1970-72 Cutlass look traditional but make upgrades hard, and this RTX system solves that. A quad pack of gauges sits on the left, an OEM-looking speedometer and programmable display in the center, and a clock with an LED bar-graph tach on the right.
>
> Integrated OEM styling keeps the familiar Oldsmobile look. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. The LED backlighting comes on in your colors, and one central control box keeps installation and setup simple.

### RTX-71C-CAP-X (p1278): 1971-76 Chevy Caprice/ Impala RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> This bolt-in RTX upgrade for 1971-76 Chevy full-size cars keeps the best of the stock design. It adds color-changeable LED backlighting and a vibrant TFT message center you can set to show the data you want.
>
> Senders for oil pressure, temp and speed are included, each with a 10 ft harness. An optional BIM-01-2 ties it into a stock or aftermarket EFI system. The bezel isn't included, so use an OEM or reproduction one. Cars with factory A/C need some changes to the stock gauge bezel ductwork. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-71D-CHG-X (p1356): 1971-74 B-Body Rallye: Plymouth GTX, RoadRunner and Dodge Charger, '71 SuperBee RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Third-gen Chargers kept the Rallye style of mixed-size round gauges, and this RTX system keeps that B-body feel. New LED backlighting is built into the OEM headlight and wiper switch and follows the colors you pick for the gauges.
>
> It mounts right into the steel dash structure, and the OEM front gauge bezel goes over it. The bezel isn't included. It covers the 1971-74 Plymouth GTX, Road Runner and Dodge Charger and the '71 Super Bee. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and TFT message centers show the extra readings.

### RTX-71I-SCT-X (p1409): 1971-80 International Scout II/ 1969-75 D Series Pickup and Travelall RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The Scout II has climbed the popularity mountain, and this RTX system makes a 1971-80 Scout even cooler. A bar-graph tach joins the speedometer, oil, water, fuel and volt gauges, and the LED backlighting comes on in your colors.
>
> It also fits 1969-75 D Series pickups and the 1969-75 Travelall. It uses your OEM bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup.

### RTX-73F-PU-X (p1253): 1973-79 Ford Pickup, 78-79 Bronco RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Your Dentside keeps the look of its stock gauges but gets late-model abilities. Color-changeable LED backlighting and twin TFT message centers come with this drop-in RTX system, and it can grow with late-model and diesel drivetrain swaps.
>
> It fits 1973-79 Ford pickups and 1978-79 Broncos, but not the E-Van. You'll need the stock instrument bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-73J-WAG-X (p1366): 1973-85 Jeep Wagoneer/ Cherokee & J Trucks RTX Instrument System

**What was wrong:** wording carried over from the original copy (12+ word run).

> This OE-inspired RTX gauge system drops right into the stock bezel of 1973-83 Jeep Wagoneers, 1974-83 Cherokees, 1984-85 Grand Wagoneers and 1973-85 J-Trucks. It keeps the stock look until the key turns and the LED backlighting comes on in your colors.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and TFT message centers show extra readings.

### RTX-77C-CAP-X (p1298): 1977-90 Chevy Caprice/ Impala & 1984-86 Pontiac Parisienne RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The Box Chevy suits an understated stock look, and this RTX system keeps it. It's a direct bolt-in with color-changing backlighting, full-color digital screens and mobile-app compatibility.
>
> It fits 1977-90 Chevy B-bodies and the 1984-86 Pontiac Parisienne, in the stock dash opening. The front dash bezel isn't included. Some wiring is needed to finish the conversion, and setup is easy with a stock drivetrain or an LS swap. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-78C-MC-X (p1188): 1978-88 Chevy Monte Carlo, 1978-87 Chevy El Camino/ Malibu/ Caballero RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Both ends of the G-body run are covered here: pick the early 1978-85 style or the late 1986-88 style of the round-gauge cluster. Either way you get the factory look with full-color LED backlighting and TFT message center displays.
>
> It's a direct fit for Monte Carlo, Malibu and El Camino with the round-gauge cluster, and you install it in your stock cluster. It doesn't fit the rectangular sweep-style cluster. The bezels and housing aren't supplied. A metric version of each style is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-78C-VET-X (p1262): 1978-82 Chevy Corvette RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Late C3 Corvettes offer plenty of performance, and this direct-fit RTX system brings the gauges up to today's standards. Your 1978-82 Corvette keeps a very stock look and gets two TFT message centers, LED backlighting and an analog clock.
>
> Install it with your stock gauge bezels. The center console trim bezel isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-79F-MUS-X (p1372): 1979-86 Ford Mustang RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Early Fox body Mustangs from 1979-86 get a factory-looking cluster with modern tech inside. The layout, faces and indicators copy the original design well enough to pass for stock, until the key turns and the LED backlighting comes on in your colors.
>
> TFT message centers show just about any reading you want. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-80F-PU-X (p1405): 1980-86 Ford Pickup and Bronco RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Bullnose 1980-86 Fords aren't just farm workhorses anymore, and this RTX system suits the builds coming back on the road with all kinds of engines. It also fits the Bronco, and it keeps the factory look until the LED backlighting comes on in your colors.
>
> It uses your OEM bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-80T-FJ-X (p1422): 1980-90 Toyota FJ60 RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Overlanders and collectors love the tough, simple 1980-90 Toyota FJ60. Whether it runs the 4.2L inline-six or a late-model LS, this direct-fit RTX system gives you the standard gauges and indicators, plus a lot more information on the built-in TFT screens.
>
> Two versions are offered. One copies the 1980-87 look, and the other matches the 1988-90 design. It fits your factory bezel, which isn't included. A metric version of each is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. The LED backlighting comes on in your colors.

### RTX-82C-CAM-X (p1407): 1982-89 Camaro RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Third-gen Camaros are turning into collector cars, and this RTX system updates the 1982-89 dash. It keeps the factory look until the key turns and the LED backlighting comes on in your colors, and TFT message centers show just about any reading you want.
>
> It doesn't fit the Berlinetta digital dash. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup.

### RTX-82P-FIR-X (p1417): 1982-92 Pontiac Firebird RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Pop-up headlights, a low body and a driver-focused cabin made the 1982-92 Firebird a defining '80s sports coupe. This direct-fit RTX system is themed after the sporty 1986-92 version and bolts into any 1982-92 non-digital dash.
>
> It won't replace the factory digital dash. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, TFT message centers show extra readings, and the LED backlighting comes on in your colors.

### RTX-83L-DEF-X (p1428): 1983-98 Land Rover Defender, Non Puma RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Boxy aluminum, exposed hinges and a bare-bones cabin make the Land Rover Defender a favorite for outdoor fans. This direct-fit RTX system lets you watch whatever engine is under the hood on the trail or the road.
>
> It fits 1983-98 non-Puma dashes. Speed, tach, water temp and fuel are analog, while oil pressure and volts read as LED bar graphs. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup.

### RTX-84B-REG-X (p1294): 1984-87 Buick Regal and Grand National RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A large, sweeping horizontal speedometer recalls the Buick design in this stock-looking cluster for the Regal, T-Type and Grand National. A bar-graph tach sits above it, hidden analog oil pressure and water temp gauges sit at the edges, and two programmable TFT message centers sit in between. A digital voltmeter makes six gauges.
>
> The bezel isn't included. Adding the SEN-09-7 puts boost in the message center, and a Grand National version with it is listed. Grand National ignitions may need the SGI-17 for the tach. Metric versions are a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and one central control box keeps installation simple.

### RTX-86J-WAG-X (p1379): 1986-91 Jeep Wagoneer & 1986-88 J Trucks RTX Instrument System

**What was wrong:** wording carried over from the original copy (12+ word run).

> Billed as "The Ultimate Wagon" in the mid '80s, the Jeep Wagoneer is coming back strong. This direct-fit RTX system fits the 1986-91 Wagoneer and 1986-88 J-Trucks, keeping the stock look until the LED backlighting comes on in your colors.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and TFT message centers show extra readings.

### RTX-87F-MUS-X (p1354): 1987-89 Ford Mustang RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> For a 1987-89 Fox Body Mustang, this RTX system is the missing piece of the interior. It looks nearly identical to the factory cluster but is loaded with technology behind the scenes, and the LED backlighting comes on in your colors.
>
> It works with a stock 5.0 or a modern swap, any combination. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. One central control box keeps installation and setup simple.

### RTX-87F-PU-X (p1406): 1987-91 Ford Pickup and Bronco RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Six analog gauges, twin TFT message centers and a row of LEDs for the warning indicators bolt into a 1987-91 Ford F-Series truck. It also fits the 1987-91 Bronco, but not the Bronco II.
>
> It uses your existing OEM front bezel, which isn't included. It works with stock drivetrains or custom swaps, and the speedometer runs from a mechanical drive or an existing vehicle speed sensor. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-88C-PU-X (p1424): 1988-91 Chevy/ GMC Pickup/ Suburban/ Tahoe/ Yukon RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Rounded lines and flush headlights marked the all-new 1988 GM truck we now call the OBS. This RTX system keeps a factory look in that dash until the LED backlighting comes on in your colors, and TFT message centers add extra readings.
>
> It fits 1988-91 Chevy and GMC pickups, plus the Suburban, Tahoe and Yukon. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup.

### RTX-90C-CAM-X (p1408): 1990-92 Camaro RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1990-92 Camaros closed out the third-gen era, and this RTX system helps keep them on the road. It looks like the factory cluster until the LED backlighting comes on in your colors, with TFT message centers for extra readings.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors are included, each with a 10 ft harness, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-90F-MUS-X (p1360): 1990-93 Ford Mustang RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Keeping a 1990-93 Fox body alive? This direct-fit RTX gauge system keeps an eye on what's happening under the hood, with TFT message centers and LED backlighting in your colors, behind a factory look.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors are included, each with a 10 ft harness. A two-sided rocker switch handles setup, and one central control box keeps installation simple.

### RTX-91T-FJ-X (p1414): 1991-97 Toyota FJ RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1991-97 Toyota FJ80 Land Cruiser is a go-anywhere legend, and this direct-fit RTX gauge system makes it even better. The turn signals show in the factory spots between the speedometer and tach.
>
> Separate LED indicators run along the bottom for 4WD, check engine, cruise control, high beam and parking brake, plus the center, front and rear diffs. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. TFT message centers show just about any reading you want, and the LED backlighting comes on in your colors.

### RTX-92C-PU-X (p1420): 1992-94 Chevy/ GMC Pickup/ Suburban/ Tahoe/ Yukon RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> In a bone stock cab or a full custom interior, this RTX system looks right at home in a 1992-94 OBS truck. It keeps a factory look until the LED backlighting comes on in your colors, and TFT message centers add extra readings.
>
> It fits 1992-94 Chevy and GMC pickups, plus the Suburban, Tahoe and Yukon. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup.

### RTX-92F-PU-X (p1411): 1992-96 Ford Pickup, and Bronco RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Ninth-gen 1992-96 Ford trucks are loved for their boxy style and toughness, and this RTX system brings modern instruments to them. It keeps the factory look until the LED backlighting comes on in your colors, with TFT message centers for extra readings.
>
> It uses your OEM bezel, which isn't included. If you keep the stock ECU and transmission, you'll need to keep the factory PSOM, which comes out of the stock cluster. The install manual explains how. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup.

### RTX-94F-MUS-X (p1427): 1994-04 Ford Mustang RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Street builds and drag racers keep the 1994-2004 SN95 Mustang popular. This RTX series adds a modern touch to the interior, with one version themed for 1994-98 cars and another for 1999-2004 cars.
>
> It uses your OEM or reproduction bezel, which isn't included. A metric version of each is a special order. The required oil pressure, water temperature and speed sensors are included, so in many cases you won't need extra parts.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. The gauges keep a factory look until the LED backlighting comes on in your colors, and TFT message centers show extra readings.

### RTX-95C-PU-X (p1418): 1995-98 Full-size, 1995-00 SUV & HD Pickup Chevy/ GMC RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> GM gave its 1995 trucks and SUVs a rounder, driver-oriented dash for the last run of the OBS era. This RTX system was made to match that layout, with the factory look until the LED backlighting comes on in your colors.
>
> It fits 1995-98 full-size pickups and 1995-2000 SUV and HD models. It uses your OEM or reproduction bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and TFT message centers show extra readings.

### RTX-97C-CAM-X (p1423): 1997-02 Camaro RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> From the base V6 to the LS1-powered Z28 and SS, the 1997-2002 Camaro closed out the fourth generation with sharp handling and muscular lines. This RTX system brightens up the dash, with a speedometer that reads to 150 mph.
>
> It fits coupes and convertibles. It uses your OEM or reproduction bezel, which isn't included. For OE or aftermarket fuel injection, the page suggests pairing it with the BIM-01-2. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. A two-sided rocker switch handles setup, and the LED backlighting comes on in your colors.

### RTX-97F-PU-X (p1412): 1997-04 Ford Full Size Pickup, and Expedition RTX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Contractors, farmers and families made the 1997-2004 Ford trucks a favorite, and collectors want them now. This RTX system fits full-size Ford pickups and the Expedition, with the factory look and LED backlighting in your colors.
>
> It doesn't fit the Ranger. It uses your OEM bezel, which isn't included. A metric version is a special order.
>
> Each RTX housing is CNC machined, with electronics Dakota Digital designs and builds in-house. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. A two-sided rocker switch handles setup, and TFT message centers show extra readings.

### VHX-1014 (p726): VHX-1014: Universal Dual 5.4" Round, Analog VHX Instrument

**What was wrong:** wording carried over from the original copy (12+ word run).

> The dual round gauge format has been a staple for generations, and this universal VHX pair fits nearly any type of vehicle. Each gauge is 5.4 inches, with lit needles over backlit faces and LCD message centers for trip meters and a 0-60 timer.
>
> The cutout is 5 inches and the depth is 1.85 inches. The housings are machined from 6061 aluminum and chrome plated. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors are included, each with a 10 ft harness. Stepper motors move the needles, and the included pushbuttons handle calibration. VHX is engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-1018 (p846): VHX-1018: Universal 4.4" x 11.4" Rounded Rectangle, Analog VHX Instrument

**What was wrong:** wording carried over from the original copy (12+ word run).

> Sized for a custom dash, this universal rounded-rectangle VHX cluster holds six analog gauges with lit needles and backlit faces, along with LCD message centers. It measures 11.4 by 4.4 inches, sized for a custom dash.
>
> Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. The included pushbuttons calibrate the speedometer and fuel gauge. Stepper motors drive the needles, and the sensors are solid state. VHX is engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-1100 (p878): VHX-1100: Universal 6" x 10.75" Competition, Analog VHX Instrument

**What was wrong:** wording carried over from the original copy (12+ word run).

> Part race gauge, part street instrument, this universal VHX-1100 pairs a speedometer that reads to 160 mph and a tach that reads to 10,000 rpm with large-sweep oil pressure and temp gauges. Four programmable message centers leave lots of room for more readings.
>
> The billet aluminum faceplate is powdercoated flat black and machined for a multi-layered look, with exposed stainless hardware. It measures 10.75 by 6 inches overall and needs a 10.25 by 5.5 inch cutout. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Fully lit needles ride on micro-controlled stepper motors, and the sensors are solid state. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-35F (p876): 1939 Ford Car VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Outfit an often-overlooked 1939 Ford with chrome and modern instruments that keep a classic look. This direct-fit VHX system has real needles that light up, backlit faces and LCD message centers for trip meters, a 0-60 timer and quarter-mile times.
>
> It comes with a new chrome bezel and also fits the 1935-36 Ford car. Overall size is 11.38 by 4.63 inches, and the cutout is 11 by 4.19 inches. Pick black or silver alloy faces in blue, red or white. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. Precision stepper motors drive the needles. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-37C (p881): 1937-38 Chevy Car VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Fully lit needles, backlit faces and LCD message centers fit right into the dash of a 1937-38 Chevy car with this VHX system. A triple-plated chrome, machined aluminum instrument housing is included.
>
> Faces come in black or silver alloy, and you can order blue, red or white. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. Micro-controlled stepper motors move the needles, and the included pushbuttons handle calibration. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-39C (p971): 1939 Chevy Car VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A triple-plated chrome, machined aluminum instrument housing comes with this VHX system, and it fits right into the dash of a 1939 Chevy car. Fully lit needles, backlit faces and LCD message centers fill it.
>
> Faces come in black or silver alloy, and you can order blue, red or white. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors are included, each with a 10 ft harness, and the speed sensor needs about 5 inches of clearance. Micro-controlled stepper motors move the needles, and the included pushbuttons handle calibration. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-42F (p1003): 1942-48 Ford/ Mercury Car VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1942 Ford dash was put on hold for WWII, then came back for 1946-48. This direct-fit VHX system brings a round billet aluminum bezel plated in chrome, plus six analog readings and two LCD message centers.
>
> The new chrome bezel for the speedometer and clock is included. Keep your stock trim panel for the rectangular satellite gauges. A matching clock for the passenger side is sold separately. It also fits 1942-48 Mercury cars. Faces come in black or silver alloy, and you can order blue, red or white. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. VHX is built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-47C-PU (p723): 1947-53 Chevy/ GMC Pickup VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The dual-round gauge layout in 1947-53 Chevy and GMC trucks has always made it hard to get more information. This VHX system puts six analog instruments and two LCD message centers in those two openings. The needles are fully lit, the faces are backlit, and the LCDs are easy to see.
>
> Custom-machined chrome bezels come in the box, and they drop right into the stock gauge openings on Chevy and GMC trucks. The system needs a 5.2 inch opening and measures 5.95 inches overall. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Micro-controlled stepper motors move the needles, and the sensors are solid state. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-50M (p797): 1950-51 Mercury VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Three LCD message centers sit among six analog readouts in this VHX system for the 1950-51 Mercury. Buttons built into the system handle programming, and the needles light up over backlit faces.
>
> It bolts to the stock cast housing. Faces come in black or silver alloy, and you can order blue, red or white. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. Precision stepper motors drive the needles. VHX is engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-53C (p844): 1953-54 Chevy Car VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> This all-new VHX system drops straight into the stock or reproduction gauge bezel of a 1953-54 Chevy car. Real needles light up over backlit faces, and LCD message centers add trip meters and a 0-60 timer.
>
> Because of the unique dash in these cars, some steel in the stock dash needs trimming to make room for the larger cluster. The bezel isn't included. Faces come in black or silver alloy, and you can order blue, red or white. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors are included, each with a 10 ft harness. Stepper motors drive the needles, and the included pushbuttons handle calibration. VHX is built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-54C-PU (p724): 1954 Chevy Pickup VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The curvy lines of the 1954 Chevy pickup made it an instant classic. VHX adds lit needles, backlit faces and easy-to-read LCD message centers, with displays you can customize.
>
> Fully machined, show-chromed bezels are included, so installation is easy. It also fits the 1955 first-series pickup, but not GMC. It needs a 6.15 inch opening and measures 6.4 inches overall. Pick black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Under the faces are micro-controlled stepper motors and solid-state sensors. Like every Dakota Digital system, it's built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-55C (p719): 1955-56 Chevy Car VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The '55-56 Chevy dash doesn't tell you much from the factory. This VHX system keeps that iconic cluster and fills it with six analog needles that light up, plus two LCD message centers. The faces are backlit, and the LCDs adjust their contrast so you can read them in bright sun.
>
> Use your factory or reproduction bezel. It's sold separately. The factory gear indicator goes away, so add the GSS-3000 if you want the gear shown in words in the message centers. Faces come in black alloy, silver alloy or a carbon fiber look, and you can order blue or red. A matching clock, analog or digital, is made for VHX gauges. A metric version is a special order.
>
> Precision stepper motors drive the needles, and the sensors are solid state. It's engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-56F-PU (p818): 1956 Ford Pickup VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The one-year-only 1956 F100 gets modern function without losing its timeless look. Lit needles over backlit faces and LCD message centers show trip meters, a 0-60 timer and quarter-mile times.
>
> It bolts into the stock dash with an original or reproduction bezel. The factory bezel isn't included. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor works with Ford or GM style cables. The included pushbuttons handle calibration. VHX is built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-58C-IMP (p877): 1958 Chevy Impala VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Recreating the American Graffiti Impala or building a modern bruiser? This bolt-in VHX system fits the 1958 Chevy Impala. Red, blue or white LED backlighting sets off silver or black alloy faces, and billet pushbuttons stick out of the original odometer opening.
>
> The OEM dash, trim, bezel and fascia aren't included. Add the matching VLC-58C analog clock for the passenger side. It can't be used alone. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. Stepper motors drive the lit needles. VHX is built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-58C-VET (p806): 1958-62 Chevy Corvette VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Chrome rings around aviation-style gauges make the 1958-62 Corvette dash unmistakable. This VHX package keeps that look with lit needles, backlit faces and LCD message centers.
>
> New chrome triple-plated, machined aluminum gauge bezels are included, and the system bolts directly into your existing cast gauge pods. A matching clock, analog or digital, is sold separately. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Micro-controlled stepper motors move the needles, and the sensors are solid state. The included pushbuttons handle calibration. VHX is engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-59C-IMP (p745): 1959-60 Chevy Impala/ El Camino VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> The 1959-60 Chevy dash was a home run then, and it's still popular today. This VHX system brings modern information to that classic design, with lit needles, backlit faces and easy-to-read LCD message centers.
>
> Every 1959-60 Chevy full-size car, El Camino included, takes it in the stock instrument housing with no alterations. The system installs into the stock cast dash pods, which aren't included. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Micro-controlled stepper motors and solid-state sensors do the work behind the faces. The included pushbuttons handle calibration. Like every Dakota Digital system, VHX is built in Sioux Falls, South Dakota, and has a limited lifetime warranty.

### VHX-60C-PU (p774): 1960-63 Chevy Pickup VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Builders often overlook the wide-open instrument housing in 1960-63 Chevy pickups. This VHX system fills it with six analog readouts and twin LCD message centers. The needles light up and the faces are backlit.
>
> It uses your stock bezel, which isn't included. It doesn't fit GMC models. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Stepper motors drive the needles, solid-state sensors feed the readings, and the included pushbuttons calibrate the speedometer and fuel gauge. Water temperature, oil pressure and speed sensors come with 10 ft harnesses. VHX is built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-61C-IMP (p824): 1961-62 Chevy Impala VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> No modification needed for a 1961-62 Impala: this VHX system fits right into the stock dash. The upper display holds the speedometer, voltmeter, fuel level and message centers, and the lower displays hold the tach, oil pressure and water temp.
>
> The upper display reuses the stock trim ring. The lower ones come with new machined, chromed aluminum housings. The dash and the chrome speedometer trim and bezel aren't included. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Stepper motors drive the lit needles, and the sensors are solid state. The included pushbuttons handle calibration. VHX is built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-64P-GTO (p856): 1964-67 Pontiac GTO/ LeMans/ Tempest VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Finish off a 1964-67 GTO, LeMans or Tempest, including the 1963 Tempest, with full analog instruments and LCD message centers in a classic design. Real needles light up over backlit faces.
>
> It fits directly into the stock Pontiac gauge carrier and uses the stock instrument housing. New clear lenses come in the kit, so the stock lenses aren't used. The bezel, trim and fascia aren't included. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Stepper motors drive the needles, and the sensors are solid state. The included pushbuttons handle calibration. VHX is engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-66F-BRO (p780): 1966-77 Ford Bronco VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Out on the trail, knowing your vitals can save you. This VHX system fits six analog readouts and two high-contrast LCD message centers inside the stock speedometer housing of a 1966-77 Bronco. It's water resistant and keeps the dash uncluttered so you can watch the trail.
>
> The bezel isn't included, so use an OEM or reproduction one. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Real needles light up over backlit faces, driven by stepper motors. Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the included pushbuttons handle calibration. VHX is built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-67C-P (p776): 1967-72 Chevy/ GMC Pickup VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Pick a third LCD message center or an analog clock for the spot above the column in your 1967-72 GM pickup. Six analog instruments fill the rest of the seven-hole bezel, with lit needles and backlit faces.
>
> It fits 1967-72 GM pickups, Blazers and Suburbans, and the stock turn signals are upgraded with LEDs. It uses a stock or reproduction front dash bezel, sold separately, and a replacement bezel is listed with this kit. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Micro-controlled stepper motors move the needles, and the sensors are solid state. The included pushbuttons handle calibration. VHX is engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-69C-CAC (p849): 1969 Camaro with Console gauges VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> For a 1969 Camaro with the console gauge option, this VHX system modernizes the dash and the console. Lit needles sit over backlit faces, and LCD message centers show trip meters and a 0-60 timer.
>
> It attaches directly to the back of the stock instrument cluster and center console housing, so installation is simple. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors are included, each with a 10 ft harness. Stepper motors drive the needles, and the included pushbuttons handle calibration. VHX is engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-69C-CAM (p722): 1969 Camaro VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Lit needles and backlit faces bring a 1969 Camaro dash up to today's standards. The LCD message centers show trip meters, 0-60 times and quarter-mile times, and you can customize what they display.
>
> The system fits right into the stock Camaro gauge carrier and keeps your factory bezel. New clear lenses come in the kit, so the stock lenses aren't used. If you need a carrier, a reproduction one is sold separately. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Micro-controlled stepper motors move the needles, and the sensors are solid state. The included pushbuttons calibrate the speedometer and fuel gauge. VHX is engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-70B-SKY (p949): 1970-72 Buick Skylark VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> A 1970-72 Buick Skylark gets six analog gauges with lit needles, backlit faces and easy-to-read LCD message centers. You can customize what the displays show.
>
> It needs the factory bezel, which isn't included. Faces come in black or silver alloy, and you can order blue, red or white. A metric version is a special order.
>
> Water temperature, oil pressure and speed sensors come with 10 ft harnesses, and the speed sensor needs about 5 inches of clearance. Micro-controlled stepper motors move the needles, and the included pushbuttons handle calibration. VHX is built in Sioux Falls, South Dakota, with a limited lifetime warranty.

### VHX-70C-CAM (p777): 1970-81 Camaro VHX Instruments

**What was wrong:** wording carried over from the original copy (12+ word run).

> Any 1970-81 Camaro can bolt in this full-function VHX system and keep its classic look. Real needles light up over backlit faces, and LCD message centers show trip meters, a 0-60 timer and quarter-mile times.
>
> It's a direct fit that uses a stock or reproduction bezel, sold separately. It doesn't fit the Firebird. Faces come in black alloy, silver alloy or a carbon fiber look, in blue or red. A metric version is a special order.
>
> Micro-controlled stepper motors move the needles, and the sensors are solid state. The included pushbuttons calibrate the speedometer and fuel gauge. VHX is engineered and built in Sioux Falls, South Dakota, with a limited lifetime warranty.

## Short rewrites (under 90 words on purpose)

| File | Words | Why |
| --- | --- | --- |
| `101069-c-p592.md` | 81 | Parts list only: cup finishes, pull block, screws and bar mount sizes |
| `101073-C-p593.md` | 80 | Parts list only: backplate, harness, lens and speed parts |
| `101160-C-p597.md` | 65 | Parts list only: cup finishes, pull block and screw |
| `101194-C-p711.md` | 76 | Parts list only: bezels, backplate, clamp and two harnesses |
| `1300-p579.md` | 88 | Parts list only: senders, bushings, speed generators and buttons |
| `1300-p580.md` | 84 | Parts list only: senders, bushings, speed generators and buttons |
| `1300-p581.md` | 86 | Parts list only: senders, bushings, speed generators and buttons |
| `130011-p1140.md` | 74 | One-part page: cable length, ends and use |
| `130048-36-p1245.md` | 54 | Page lists only three cable styles and their fit; nothing more to say without padding |
| `130085-p1436.md` | 44 | Page gives only the port size, material and included hardware |
| `300056-p715.md` | 34 | Parts list only: two screws for four bracket models |
| `300076-p707.md` | 45 | Parts list only: screws and four clamps |
| `392004-p716.md` | 44 | One-part page: button with boot and the gauges it fits |
| `393106-p1279.md` | 72 | Parts list only |
| `394024-p708.md` | 40 | Parts list only: harness and button |
| `394046-p709.md` | 32 | Parts list only: two harnesses |
| `620001-p1214.md` | 66 | Parts list only: sensor, cables, adaptor and plug |
| `620008-p1142.md` | 41 | Page gives only fit, size and thread |
| `BCL-1L-p1113.md` | 51 | Page gives only pull side, pin and size |
| `BCL-2-p94.md` | 54 | Page gives only pairs, pins, size and fastener note |
| `BD-140-p668.md` | 76 | Page gives only fit, display colors, kept parts and warranty |
| `BIM-05-1-p756.md` | 68 | Page gives only the reading mix, sender and module fit |
| `BIM-16-1-p759.md` | 88 | Page gives only fit, time formats and module note |
| `BIM-17-2-p760.md` | 78 | Page gives only compass points, temp reading and module fit |
| `BIM-19-2-p761.md` | 88 | Page gives only the bag layouts, tank reading, sender and module fit |
| `BKT-3-p253.md` | 36 | Page gives only fit, bar sizes and finish |
| `BKT-33-p503.md` | 31 | Page gives only fit, bar sizes and finish |
| `BKT-50-p248.md` | 58 | Page gives only fit, widths and finish |
| `BKT-500-p249.md` | 37 | Page gives only fit, bar sizes and finish |
| `BKT-5002-p250.md` | 86 | Page gives only the three clamp styles, finishes and fit |
| `BKT-5009-p251.md` | 52 | Page gives only fit, riser styles and finish |
| `BKT-5012-p255.md` | 36 | Page gives only fit and the housing list |
| `BKT-7020-p252.md` | 26 | Page gives only fit and finish |
| `BZL-3000-K-p704.md` | 89 | Parts list only |
| `CMD-10K-p89.md` | 75 | Page lists kits, warranty and relay note only |
| `CMD-2000-p91.md` | 36 | Page gives only what it controls and what is not included |
| `CMD-4000-p92.md` | 40 | Page gives only the lockout feature and actuator options |
| `CMD-X-p90.md` | 65 | Page gives only outputs, uses, remotes, relays and warranty |
| `CUP-3001-p254.md` | 48 | Page gives only the two cup versions and their mounting |
| `CUP-3301-p502.md` | 36 | Page gives only use and two finishes |
| `CUP-4001-p545.md` | 38 | Page gives only fit, two finishes and gauge note |
| `DCC-2200-p475.md` | 87 | Page gives only fit, display, finish, warranty and compatibility |
| `DGS-1-p64.md` | 53 | Page gives only colors, fit, dimming and size |
| `DGS-3-p63.md` | 80 | Page gives only readings, size, colors, finish and sender note |
| `DGS-4-p62.md` | 78 | Page gives only readings, size, colors, finish and sender note |
| `DGS-p482.md` | 76 | Page gives only mounting, size, material and options |
| `DIM-1-p404.md` | 72 | Page gives only use, fit and hole size |
| `DP-1-p87.md` | 30 | Page gives only size, stroke, force and pairs |
| `DP-3-p395.md` | 26 | Page gives only stroke, length and force |
| `GSS-3000-p1222.md` | 84 | Page gives only fit, mounting and what it replaces |
| `Gift-p578.md` | 50 | Page gives only the gift idea and amounts |
| `HLC-2162-p1202.md` | 66 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-301-p260.md` | 58 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3011-p262.md` | 52 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3016-p264.md` | 83 | Page gives only the readings, compatibility, warranty and odometer note |
| `HLY-3021-p263.md` | 33 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3027-p261.md` | 31 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3032-p270.md` | 47 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3041-p425.md` | 33 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3051-p280.md` | 25 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3061-p282.md` | 29 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3073-p272.md` | 32 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3111-p276.md` | 28 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3191-p274.md` | 44 | Thin page: only size, fit, range, warranty and manual notes |
| `HLY-3401-p490.md` | 79 | Page gives only readings, sender notes and warranty |
| `HLY-3402-p331.md` | 43 | Thin page: only size, fit, range, warranty and manual notes |
| `IND-1A-p1246.md` | 57 | Thin page: only size, fit, range, warranty and manual notes |
| `ION-01-6-p291.md` | 95 | Page gives only styling, options and odometer note |
| `ION-03-1-p324.md` | 59 | Page gives only range, finishes and sender note |
| `ION-04-1-p362.md` | 70 | Page gives only range, finishes and sender list |
| `ION-05-1-p356.md` | 45 | Ion gauge page: range, sensor and finish options only |
| `ION-06-1-p353.md` | 63 | Ion gauge page: range, sensor and finish options only |
| `ION-14-1-p542.md` | 57 | Ion gauge page: range, sensor and finish options only |
| `ION-15-1-p543.md` | 52 | Ion gauge page: range, sensor and finish options only |
| `ION-16-1-S-T-p505.md` | 37 | Ion gauge page: range, sensor and finish options only |
| `ION-20-1-p544.md` | 53 | Ion gauge page: range, sensor and finish options only |
| `KN-3-p59.md` | 34 | Page gives only fit and thread for two nuts |
| `LACT-MNT-p1196.md` | 37 | Page lists only the two hardware kits |
| `LAT-NLF-p652.md` | 49 | Page gives only use and current rating |
| `LOK-1601-p56.md` | 29 | Page gives only the two cable versions |
| `MBM-09-p1312.md` | 48 | Page gives only fit, range and contents |
| `MBM-17-p1313.md` | 41 | Page gives only fit, GPS note and add-on sensor |
| `MBM-19-p1314.md` | 70 | Page gives only fit and contents |
| `MCH-GPS17-p953.md` | 55 | Page gives only fit, readings, antenna note and bezels |
| `MCL-4013R-p537.md` | 31 | Page gives only size, units and colors |
| `MCL-4027R-p538.md` | 23 | Page gives only size, colors and warranty |
| `MCL-4032R-p539.md` | 42 | Page gives only range, senders, colors and warranty |
| `MCL-4073R-p576.md` | 48 | Page gives only range, sender, colors and warranty |
| `MCL-5100-p598.md` | 73 | Page gives only style, fit notes and odometer note |
| `MCL-5200-K-p599.md` | 67 | Page gives only style, fit notes and odometer note |
| `ODY-01-3-p296.md` | 86 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-02-7-p297.md` | 61 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-03-1-p321.md` | 85 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-04-1-p383.md` | 78 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-05-1-C-T-p357.md` | 59 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-06-1-p380.md` | 83 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-07-1-p325.md` | 76 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-09-5-p377.md` | 87 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-10-2-p381.md` | 85 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-12-1-p379.md` | 88 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-14-1-p316.md` | 78 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-15-1-C-B-p318.md` | 74 | Odyssey gauge page: range, sensor, options and warranty only |
| `ODY-16-1-p344.md` | 57 | Gauge page: range, sensor, options and warranty only |
| `ODY-19-1-p388.md` | 84 | Gauge page: range, sensor, options and warranty only |
| `ODY-20-1-C-B-p744.md` | 72 | Gauge page: range, sensor, options and warranty only |
| `OHC2-95C-PU-p396.md` | 51 | Thin page: little beyond the part list or one-line description |
| `PAC-3100-p464.md` | 62 | Thin page: little beyond the part list or one-line description |
| `PAC-3200-p465.md` | 59 | Thin page: little beyond the part list or one-line description |
| `PAC-3500-p460.md` | 25 | Thin page: little beyond the part list or one-line description |
| `PDR-1-p85.md` | 55 | Thin page: little beyond the part list or one-line description |
| `PDR-2-p86.md` | 52 | Thin page: little beyond the part list or one-line description |
| `PGR-1-p496.md` | 62 | Thin page: little beyond the part list or one-line description |
| `RET-2001-S-p227.md` | 79 | Thin page: little beyond the part list or one-line description |
| `RLY-1-p83.md` | 12 | Thin page: little beyond the part list or one-line description |
| `RLY-2-p84.md` | 14 | Thin page: little beyond the part list or one-line description |
| `RLY-3-p642.md` | 15 | Thin page: little beyond the part list or one-line description |
| `SEN-01-1-p620.md` | 48 | Thin page: little beyond the part list or one-line description |
| `SEN-01-2-p588.md` | 58 | Thin page: little beyond the part list or one-line description |
| `SEN-01-5-p1248.md` | 109 | Thin parts or sender page: only fit, range and part list |
| `SEN-01-5-p729.md` | 107 | Thin parts or sender page: only fit, range and part list |
| `SEN-01-5-p730.md` | 109 | Thin parts or sender page: only fit, range and part list |
| `SEN-03-1-p110.md` | 88 | Thin parts or sender page: only fit, range and part list |
| `SEN-03-1-p124.md` | 54 | Thin parts or sender page: only fit, range and part list |
| `SEN-04-1-p111.md` | 75 | Thin parts or sender page: only fit, range and part list |
| `SEN-04-3-p113.md` | 24 | Thin parts or sender page: only fit, range and part list |
| `SEN-04-3-p114.md` | 44 | Thin parts or sender page: only fit, range and part list |
| `SEN-04-p582.md` | 68 | Thin parts or sender page: only fit, range and part list |
| `SEN-04-p583.md` | 81 | Thin parts or sender page: only fit, range and part list |
| `SEN-06-1-p112.md` | 24 | Thin parts or sender page: only fit, range and part list |
| `SEN-1011-p242.md` | 53 | Thin parts or sender page: only fit, range and part list |
| `SEN-1012-p243.md` | 50 | Thin parts or sender page: only fit, range and part list |
| `SEN-1017-p244.md` | 59 | Thin parts or sender page: only fit, range and part list |
| `SEN-1018-p245.md` | 59 | Thin parts or sender page: only fit, range and part list |
| `SEN-1019-p246.md` | 51 | Thin parts or sender page: only fit, range and part list |
| `SEN-1031-p328.md` | 51 | Thin parts or sender page: only fit, range and part list |
| `SEN-1039-p1018.md` | 41 | Thin parts or sender page: only fit, range and part list |
| `SEN-1043-p329.md` | 85 | Thin parts or sender page: only fit, range and part list |
| `SEN-11-4-p115.md` | 33 | Thin parts or sender page: only fit, range and part list |
| `SEN-12-4-p116.md` | 39 | Thin parts or sender page: only fit, range and part list |
| `SEN-12-p758.md` | 87 | Thin parts or sender page: only fit, range and part list |
| `SEN-15-1-p120.md` | 8 | Thin parts or sender page: only fit, range and part list |
| `SEN-20-3-p123.md` | 15 | Thin parts or sender page: only fit, range and part list |
| `SEN-201-p983.md` | 26 | No description on the page: only the part names |
| `SEN-23-1-p121.md` | 18 | Page gives only range and thread |
| `SEN-3111-p330.md` | 17 | No description on the page: only the title and the HLY-3111 sensor note |
| `SGI-100BT-p1192.md` | 62 | Page gives only the three functions and size |
| `SGI-17-p1103.md` | 25 | Page gives one fit sentence |
| `SGI-20-p1429.md` | 76 | Page gives only how it works |
| `SIM-1A-GL-p240.md` | 46 | Page gives only fit and use |
| `SIM-1A-M-p239.md` | 58 | Page gives only use and size |
| `SIM-1A-p1011.md` | 61 | Page gives only use, fit and size |
| `STA-1000-p825.md` | 41 | Page gives only the plug-in and outputs |
| `TSI-1-p247.md` | 36 | Page gives only fit and wiring |
| `VCM-200-p1399.md` | 62 | Page gives only the two versions, app and handles |
| `VFD3X-1002-p229.md` | 83 | Universal panel page: size and the shared spec only |
| `VFD3X-71C-IMP-p179.md` | 85 | Page gives only fit and the shared spec |
| `VHX-69C-NOV-p815.md` | 89 | Page gives only fit, bezel note and options |
| `VLC-16-1-p1013.md` | 73 | Page gives only lighting, size, options and fit |
| `VLC-16-2-p1227.md` | 55 | Page gives only size, match, options and standalone note |
| `XMT-4-p81.md` | 24 | No description on the page: title and item name only |
| `XMT-6-9K-p694.md` | 16 | Page gives only fit and manual |
| `XMT-6-p80.md` | 21 | Page gives only fit and manual |
| `p1105.md` | 30 | Discontinued placeholder page |
| `p1127.md` | 27 | Discontinued placeholder page |
| `p216.md` | 89 | Page gives only the service, prep steps, ordering, warranty and colors |
| `p285.md` | 77 | Gauge page: range, sensor, options and warranty only |
| `p287.md` | 59 | Gauge page: range, sensor, options and warranty only |
| `p289.md` | 80 | Gauge page: range, sensor, options and warranty only |
| `p292.md` | 78 | Gauge page: range, sensor, options and warranty only |
| `p294.md` | 58 | Gauge page: range, sensor, options and warranty only |
| `p308.md` | 60 | Gauge page: range, sensor, options and warranty only |
| `p315.md` | 70 | Gauge page: range, sensor, options and warranty only |
| `p319.md` | 73 | Gauge page: range, sensor, options and warranty only |
| `p322.md` | 72 | Gauge page: range, sensor, options and warranty only |
| `p326.md` | 70 | Gauge page: range, sensor, options and warranty only |
| `p332.md` | 77 | Gauge page: range, sensor, options and warranty only |
| `p345.md` | 81 | Gauge page: range, sensor, options and warranty only |
| `p347.md` | 92 | Gauge page: range, sensor, options and warranty only |
| `p349.md` | 75 | Gauge page: range, sensor, options and warranty only |
| `p358.md` | 56 | Gauge page: range, sensor, options and warranty only |
| `p360.md` | 66 | Gauge page: range, sensor, options and warranty only |
| `p363.md` | 77 | Gauge page: range, sensor, options and warranty only |
| `p365.md` | 83 | Gauge page: range, sensor, options and warranty only |
| `p368.md` | 89 | Thin page: little beyond the part list or one-line description |
| `p389.md` | 79 | Gauge page: range, sensor, options and warranty only |
| `p392.md` | 55 | Manual index page: tabs and model list only |
| `p393.md` | 67 | Manual index page: tabs and section list only |
| `p397.md` | 76 | Gauge page: range, sensor, options and warranty only |
| `p49.md` | 74 | Page gives only fit, size, finishes, warranty and manual |
| `p574.md` | 95 | Thin page: little beyond the part list or one-line description |
| `p600.md` | 33 | Discontinued placeholder page |
