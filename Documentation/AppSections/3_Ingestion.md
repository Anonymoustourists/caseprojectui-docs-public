<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

- [Transcript Extraction](#transcript-extraction)
- [Police Report Parsing](#police-report-parsing)
- [Witness Statement](#witness-statement)
- [Witness Affidavit](#witness-affidavit)
- [Warrant and Warrant Affidavit](#warrant-and-warrant-affidavit)
- [Party Pleadings](#party-pleadings)
- [Opinion and Order Parsing](#opinion-and-order-parsing)
- [Text Message / Social Media Parsing](#text-message--social-media-parsing)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Transcript Extraction

Initial pass has been created, but the output is not yet satisfactory. The goal is to extract speaker-labeled transcripts from court documents, which often have complex formatting and multiple speakers. The output should be in markdown format with clear speaker labels and timestamps where applicable.

Additionally, need to add the ability to infer speakers from context when not explicitly labeled (where table of contents indicates this is prosecutor's witness, all Qs of that witness during direct examination are by prosecutor, and all As are by the witness)

### Police Report Parsing

Need to add functionality. Including extracting and utilizing report number, case number, date, agency, etc.

Should add "Speaker" ie report author(s)

### Witness Statement

Where a non-officer witness signs a statement prepared by the police or another investigator, this is a witness statement. Need to add speaker (the witness) and date of statement.

### Witness Affidavit

Where a non-officer witness signs an affidavit prepared by the police or another investigator, this is a witness affidavit. Need to add speaker (the witness) and date of affidavit.

### Warrant and Warrant Affidavit

### Party Pleadings

Need to add ability to generate drafter, and party associated with drafter, date filed, case number, document type (motion, order, etc), and title of pleading.

### Opinion and Order Parsing

Need to add ability to generate court issuing opinion/order, date issued, case number, judge issuing opinion/order.

### Text Message / Social Media Parsing

similar to transcript extraction, except frequently the text is in images and the speaker will be labeled via social media handle or phone number. These can still be displayed as transcripts, and, will be able to be associated with Person entities' phone numbers and social media accounts. It's helpful to indicate person associated with phone number or social media handle in the transcript, but retain the number and handle, because of the possibility of multiple people using the same number or handle over time.
