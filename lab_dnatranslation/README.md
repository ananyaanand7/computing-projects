**DNA Transcription & Translation Program**

This program reads a DNA sequence from a file, transcribes it into mRNA, and then translates the mRNA into a polypeptide chain using a codon translation table.

**Features:**
- Transcription: Converts a DNA sequence into mRNA by replacing thymine (T) with uracil (U).
- Translation:
    - Locates the first start codon (AUG).
    - Reads codons in groups of three.
    - Maps each codon to its corresponding amino acid using RNA_CODON_TABLE.
    - Stops translation upon encountering a stop codon.
- File-Based Processing: Reads a DNA sequence from an input file and prints the resulting amino acid chain.

**File Structure**
project_folder/
│
├── translation_table.py   # Contains RNA_BASES and RNA_CODON_TABLE
├── sample_short.txt       # Example DNA input file
└── dna_translation.py                # (the main code)

**How to Run the Program**
1. Prepare Your DNA Input File
Create a .txt file containing a DNA sequence, for example:
ATGGTACGTTAA

2. Run the Script: Make sure translation_table.py is in the same directory.
- In the terminal: python dna_translation.py

By default, the script attempts to read: sample_short.txt)
- **To translate a different file, change the argument inside: translate_file("your_filename.txt")** 

Function Descriptions
1. transcribe(file): 
    Reads raw DNA from the input file.
    Converts all characters to uppercase.
    Replaces all T with U to form an mRNA strand.
Returns: str — the mRNA sequence.
2. translate(mrna_strand)
    Searches for the first occurrence of the start codon AUG.
    Iterates over mRNA in steps of 3 (codons).
    Converts each codon into an amino acid using: RNA_BASES.index() & RNA_CODON_TABLE
    Stops when a Stop codon is reached.
Returns: list — a list of amino acids in the polypeptide chain.
3. translate_file(filename)
    Opens the given file.
    Transcribes → translates → prints the resulting amino acid chain.

Example Output:
For an input DNA sequence: ATGGUUACGUAA...
The program may print something like:
['Met', 'Val', 'Thr']

Requirements
- Python 3.x
- translation_table.py containing:
        - RNA_BASES — list of RNA bases
        - RNA_CODON_TABLE — nested list for codon lookup

Notes
- If no start codon (AUG) is found, the function returns an empty list.
- If translation reaches the end of the mRNA without a stop codon, it returns an empty list (per assignment spec).
