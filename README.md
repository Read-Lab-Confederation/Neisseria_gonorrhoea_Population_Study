Neisseria_gonorrhoea_Population_Study

Scripts and  materials on the study on Neisseria gonorrhoea population structure and antibiotics resistance evolution.

1) blast_read.py
    Parses antibiotic resistance database for matches to genes identified in 
    BLAST search of sample set gene sequence database
    
2) parse.pl
   Searches BLAST output for varint positions that indicate resistance mutation, 
   when searching against a reference sequence for underlying resistance mutations.
   
3) noncore_parseAZ.py, noncore_parseCf.py,noncore_parseTet.py
   Searches through non-core gene clusters in sample set for presence of 
   horizontally transferred genes for the respective phenotypes of Azithromycin,
   Cefexime and Tetracycline resistance.
   
4) pheno.R
   Performs fisher's test for significance of association of presence 
   of transfered gene and antibiotic resistance phenotype
