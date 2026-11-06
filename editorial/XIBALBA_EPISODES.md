# Xibalba cycle — narrative episode inventory

**Status:** Working episode register v0.1 (2026-11-05), for editorial review. **Not** a final book outline, a manuscript transcription or an assertion that every event has been independently collated.

This is the selected Xibalba cycle in **story chronology**, not a table of contents for the entire *Popol Vuh*. Read together with the [editorial charter](PROJECT_CHARTER.md). Stable research IDs refer to [corpus events](../corpus/indexes/events.json) and [corpus passages](../corpus/indexes/passages.json). The corpus groups several scenes under one event; this register gives them smaller, independently useful **editorial beat IDs** (`XB-001` etc.). The IDs should not be recycled if a future outline rearranges scenes.

## Evidence key

- **M** — A relevant image/folio of the Ximénez manuscript was **selected and checked** in PR #4, with historical printed parallels. This does **not** certify complete transcription, expert paleography or every claim in the row.
- **P** — Printed historical passages or their concordance have been located; **direct manuscript collation is pending** for this finer beat.
- **S** — Supported at a **provisional/retelling level**, mainly by the original corpus's Spence-based episode skeleton or other uncollated descriptions. Check closer witnesses before turning these beats into detailed manuscript claims.
- **U** — Decision or interpretation remains open; no direct source event established.

`Required` means the beat should be represented or explicitly accounted for in an adaptation of the chosen cycle; it does **not** prescribe a full stanza. `Bridge` is a transitional episode that may be compressed without severing causality. `Optional` means the in-scope narrative can omit it with a recorded decision. Finer chronology of the younger twins' separate tests will need source collation before it is fixed in verse.

## Movement A — The first generation and the defeat

| Beat | What the reader must learn / what happens | Corpus ID | Evidence | Treatment |
| --- | --- | --- | --- | --- |
| XB-001 | Establish Xmucane and Xpiyacoc's family; distinguish One Hunahpu, his wife Xbaquiyalo and earlier sons Hunbatz/Hunchouen from unmarried Seven Hunahpu. | `event-fathers-family` / `pv-fathers-family` | M | Required |
| XB-002 | The older brothers play ball; the sound/observation reaches Xibalba and provokes its lords. Introduce One Death and Seven Death as hostile powers. | `event-fathers-summons` / `pv-fathers-summons` | M | Required |
| XB-003 | The four owl messengers bring an ostensibly sporting invitation with a lethal purpose. | `event-fathers-summons` | M | Required |
| XB-004 | The men leave family instructions and ball equipment behind. Xmucane's grief and the suspended/hidden equipment will matter again. | `event-fathers-summons` | M | Required |
| XB-005 | During the first descent they pass hazards but are misled at the crossroads, including the speaking black road. | `event-fathers-defeat` / `pv-fathers-defeat` | M | Required |
| XB-006 | They address wooden effigies, are mocked by the lords and sit on a heated seat. | `event-fathers-defeat` | M | Required |
| XB-007 | They fail the Dark House's torch and tobacco test and are condemned; **do not** assign the complete catalogue of later houses to them or invent a narrated fatal ball match after this failure. | `event-fathers-defeat` | M | Required |
| XB-008 | Both men are killed and buried; One Hunahpu's head alone is explicitly severed for the next episode. | `event-fathers-defeat` / `event-head-tree` | M | Required |

**Primary research:** [First Ballgame](../corpus/research/first-ballgame.md), [Head in the Tree](../corpus/research/head-in-tree.md). See manuscript selected sequences 33–40 noted there. Narrative purpose: establish the older generation's failed approach, the lords' deceit and the family inheritance that a later generation can recover.

## Movement B — The head, Xquic and contested kinship

| Beat | What the reader must learn / what happens | Corpus ID | Evidence | Treatment |
| --- | --- | --- | --- | --- |
| XB-009 | One Hunahpu's head is hung in the tree, which bears fruit; the head becomes difficult to distinguish. The lords forbid approach. | `event-head-tree` / `pv-head-tree` | M | Required |
| XB-010 | Xquic, daughter of **Cuchumaquic**, hears of the tree and deliberately goes to see it. | `event-xquic-conception` / `pv-xquic-conception` | M | Required |
| XB-011 | The head speaks about endurance in descendants; Xquic responds, extends her hand and conceives through its saliva. Do not pass a modern sexual analogy off as a K'iche' word. | `event-xquic-conception` | M | Required |
| XB-012 | The pregnancy is discovered after six months; her father consults the lords and demands her heart despite her account. | `event-xquic-escape` / `pv-xquic-escape` | M | Required |
| XB-013 | Xquic **persuades the owl messengers** not to kill her, devises the red-sap substitute heart and redirects their course. | `event-xquic-escape` | M | Required |
| XB-014 | The rulers accept and burn the substitute heart; Xquic escapes Xibalba for the living world. | `event-xquic-escape` | M | Required |
| XB-015 | Pregnant Xquic reaches Xmucane, asserts her family connection and initially meets disbelief. | `event-xquic-xmucane` / `pv-xquic-xmucane` | M | Required |
| XB-016 | Xmucane demands a netful of maize from a nearly bare field; Xquic acts upon the remaining plant/silk and receives supernatural help. | `event-xquic-xmucane` | M | Required |
| XB-017 | The net arrives full without stripping the field. Xmucane inspects the evidence and accepts Xquic. The carriers' **animal/human** descriptions diverge among editions. | `event-xquic-xmucane` | M | Required |

**Primary research:** [Head in the Tree](../corpus/research/head-in-tree.md), [Xquic: Conception and Escape](../corpus/research/xquic-conception-and-escape.md), [Xquic and Xmucane](../corpus/research/xquic-and-xmucane.md). Selected manuscript sequences 39–45. Narrative purpose: turn an underworld death into a future generation through **Xquic's decisions**, not a passive miracle. Distinguish the head-bearing tree from Hunahpu's much later **squash head**.

## Movement C — The younger generation inherits the challenge

| Beat | What the reader must learn / what happens | Corpus ID | Evidence | Treatment |
| --- | --- | --- | --- | --- |
| XB-018 | Hunahpu and Xbalanque are born; their household life begins in hardship. Xquic remains present after birth. | `event-twins-childhood` / `pv-twins-childhood` | M | Required |
| XB-019 | Older half-brothers Hunbatz and Hunchouen resent them. The younger pair's tree stratagem turns the older boys into monkeys; Xmucane cannot restore the household. | `event-twins-childhood` | P | Required |
| XB-020 | The twins work fields and hunt with blowguns; animals undo work at night, leading to encounters and new information. | `event-twins-childhood` | P | Bridge |
| XB-021 | A rat reveals the hidden ballgame inheritance. The boys arrange a distraction involving their **mother and grandmother** to retrieve the equipment. | `event-twins-ballgame` / `pv-twins-ballgame` | P | Required |
| XB-022 | The younger twins play on the old court. Xibalba hears them, and the second summons repeats the ancestral pattern. | `event-twins-ballgame` | P | Required |
| XB-023 | They tell **Xmucane and Xquic** of the journey and plant canes as signs of survival or death. | `event-twins-descent` / `pv-twins-descent` | P | Required |

**Primary research:** [Xquic and Xmucane](../corpus/research/xquic-and-xmucane.md) section “Her subsequent role”; [first-ballgame dossier](../corpus/research/first-ballgame.md). Several later references to Xquic are pinned in Scherzer; manuscript collation is still pending. Narrative purpose: show a specific **inherited challenge**, not an arbitrary second adventure. Preserve the older brothers' skill and household ties before their downfall.

## Movement D — The second descent and ordeal

| Beat | What the reader must learn / what happens | Corpus ID | Evidence | Treatment |
| --- | --- | --- | --- | --- |
| XB-024 | The twins take the dangerous roads to Xibalba, crossing the underworld's rivers and choosing their way through the crossroads. | `event-twins-descent` / `pv-twins-descent` | P | Required |
| XB-025 | They send a biting insect to reveal each lord's name, then distinguish wooden figures from real rulers and avoid the earlier men's humiliations. | `event-twins-descent` | P | Required |
| XB-026 | They overcome the torch-and-cigar challenge that defeated their elders without consuming the required objects. | `event-twins-descent` / `event-twins-trials` | P | Required |
| XB-027 | The contested ballgames involve deliberately harmful demands and rule manipulation; the twins meet the lords' tricks with their own ingenuity. | `event-twins-trials` / `pv-twins-trials` | S | Required |
| XB-028 | Ants obtain forbidden flowers for the twins, circumventing the lords' guards. Confirm its exact placement relative to the houses before finalizing the episode order. | `event-twins-trials` | S | Required |
| XB-029 | Razor/Knife House: blades threaten the twins; they use ingenuity to survive. | `event-twins-trials` | S | Required |
| XB-030 | Cold House: the freezing ordeal is overcome. | `event-twins-trials` | S | Required |
| XB-031 | Jaguar House: the beasts' danger is neutralized. | `event-twins-trials` | S | Required |
| XB-032 | Fire House: the ordeal of flames is survived. Distinguish this from the later **voluntary death by fire**. | `event-twins-trials` | S | Required |
| XB-033 | Bat House: Camazotz decapitates younger Hunahpu when he exposes his head. | `event-twins-trials` / `event-borrowed-head` | S | Required |
| XB-034 | Xbalanque gives Hunahpu a **squash replacement head**, with animal assistance; a rabbit distracts the lords at ballplay and the true head is recovered. | `event-borrowed-head` / `pv-borrowed-head` | S | Required |

**Evidence caution:** The [corpus event list](../corpus/indexes/events.json) flags the trials and borrowed-head episodes as seeded from Spence, not collated against manuscript images. The *existence* of the episodes is not presented here as controversial; their precise sequence, wording, ritual mechanics and details require earlier-witness comparison. Don't use a confident verse as a substitute for that comparison. Narrative purpose: each trial must reveal a different **strategy** or raise stakes, not become an interchangeable catalogue.

## Movement E — Chosen death, the downfall and the limits of victory

| Beat | What the reader must learn / what happens | Corpus ID | Evidence | Treatment |
| --- | --- | --- | --- | --- |
| XB-035 | The twins plan to turn the lords' intended destruction into a deliberate performance; two seers receive instructions about the remains. | `event-death-resurrection` / `pv-death-resurrection` | S | Required |
| XB-036 | They willingly enter the fire, their bones are ground and cast into water. This is **not** merely another trial house. | `event-death-resurrection` | S | Required |
| XB-037 | After a measured interval they return in altered form and then as wandering poor performers, concealing their identities. | `event-death-resurrection` | S | Required |
| XB-038 | The performers demonstrate destruction and restoration (including a house, animals and one another); the reputation of these miracles reaches the court. Avoid narrating the same trick again and again without escalation. | `event-victory` / `pv-victory` | S | Required |
| XB-039 | The rulers ask to experience resurrection. The twins kill the leading lords but **do not bring them back**. | `event-victory` | M | Required |
| XB-040 | The brothers disclose who they are and why they came. Xibalba's surviving powers submit; its authority and offerings are reduced, **not all death abolished**. | `event-victory` | M | Required |
| XB-041 | The planted canes and Xmucane's response reveal the twins' fate through withering and renewed growth; the household performs remembrance. | `event-father-reunion` / `pv-father-reunion` | M | Required |
| XB-042 | The twins seek their father and uncle. The attempt involving an ancestor's face/name does **not** accomplish complete physical restoration; exact grammar and individual ancestral referents remain under review. | `event-father-reunion` | M | Required |
| XB-043 | They promise ancestral recognition and remembrance; the earlier defeat has a meaningful answer without a simplistic reversal of mortality. | `event-father-reunion` | M | Required |
| XB-044 | The victorious pair ascend, associated with Sun and Moon. The clause's context favors the **younger twins**, but the exact individual assignment is unresolved; **no heavenly ballgame is established by the clause**. | `event-ascension` / `pv-ascension` | M | Required |
| XB-045 | The four hundred youths become celestial companions/stars in the source ending; their Zipacna episode is **out of scope** here. Decide on a brief contextual explanation or explicit omission. | `event-ascension` | M | Optional |

**Primary research:** [Ancestors and the Ascension](../corpus/research/ancestors-and-ascension.md), selected manuscript sequences 71–74; [eleven-book implications](../corpus/research/eleven-book-implications.md). The original poem extends the final departure landscape, celestial roles and heavenly ballgame; these may be literary choices but cannot be recorded as literal manuscript detail.

## Coverage and boundaries checklist

**In scope and accounted for:** earlier family/ballgame; first summons, descent, ordeal and death; fruit-bearing head; Xquic's choice, conception, threatened execution, substitute heart, flight and maize test; birth, elder brothers and childhood; retrieved equipment, second summons and survival canes; the second descent's roads, recognition and all named houses; ballgames, flowers, beheading and borrowed head; voluntary death, watery return and disguised performances; the lords' unrevived deaths, reduced powers, household memorials, ancestral limitation and ascent.

**Explicitly out of scope:** world creation, failed humans, Seven Macaw, Zipacna/Cabrakan, maize-human creation, Tulan and the dynastic/colonial histories. The four hundred youths are the one in-scope ending that refers to an excluded antecedent: decide how to handle it, don't quietly invent the missing context.

**Open source work before verse:** the youth-trial sequence needs more direct manuscript collation; the Xquic-after-birth references need a complete pass; the ancestor's face/name passage and celestial identifications need K'iche' linguistic review. All three manuscript diplomatic excerpts in the corpus are provisional. This inventory is *not* 45 independently verified manuscript passages.

## What happens next (not yet done)

1. **Author reviews the boundary**, particularly the four hundred youths and how much of the childhood should be dramatized.
2. **Editorial pass: assign narrative weights** to the 45 beats (full scene / short bridge / summary / deliberate omission), without forcing equal space or a fixed book count.
3. **Stanza audit of V1** by persistent IDs, with source and form checks. Current Books I–VII are references, not a locked structural sequence.
4. **Book architecture**: cluster weighted beats around actual dramatic turns, choose boundaries and stanza budgets, then create bounded episode briefs.
5. **Draft, review and integrate** one short episode at a time. Preserve an explicit editorial decision record.

**Important:** No changes to the seven published books, no new poetry and no claims of complete source collation are authorized by this register.
