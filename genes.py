def descargar(accs)
    from Bio import Entrez 
    from Bio import SeqIO 

    # Simple fasta en GenBank NCBI
    Entrez.email = "gualapuro.moises@gmail.com" 
    with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="accs") as genes:
        seq_record = SeqIO.read(handle, "fasta")
    print("%s with %i features" % (seq_record.id, len(seq_record.features)))
    seq_record.seq
