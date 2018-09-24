from app.view.attr import AttrH
from .view_setup import ViewSetup

#===============================================
CONFIG_ATTRS = {
    "view_gen": [
        AttrH("Gene(s)", is_seq = True),
        AttrH("hg19"),
        AttrH("hg38"),
        AttrH("Worst Annotation"),
        AttrH("Canonical Annotation"),
        AttrH("RefSeq Transcript (Canonical)", is_seq = True),
        AttrH("RefSeq Transcript (Worst)", is_seq = True),
        AttrH("Ensembl Transcripts (Canonical)", is_seq = True),
        AttrH("Ensembl Transcripts (Worst)", is_seq = True),
        AttrH("Ref"),
        AttrH("Alt"),
        AttrH("Splice Region", is_seq = True),
        AttrH("GeneSplicer", is_seq = True),
        AttrH("cPos (Worst)", is_seq = True),
        AttrH("cPos (Canonical)", is_seq = True),
        AttrH("cPos (Other)", is_seq = True),
        AttrH("pPos (Worst)", is_seq = True),
        AttrH("pPos (Canonical)", is_seq = True),
        AttrH("pPos (Other)", is_seq = True),
        AttrH("Variant Exon (Canonical)", is_seq = True),
        AttrH("Variant Exon (Worst Annotation)", is_seq = True),
        AttrH("Variant Intron (Worst Annotation)", is_seq = True),
        AttrH("Variant Intron (Canonical)", is_seq = True),
        AttrH(None),
        AttrH("Proband Genotype"),
        AttrH("Maternal Genotype"),
        AttrH("Paternal Genotype"),
        AttrH("IGV", kind="link"),
    ],
    "view_qsamples": [
        AttrH("Title"),
        AttrH("Quality by Depth"),
        AttrH("Mapping Quality"),
        AttrH("Variant Call Quality"),
        AttrH("Strand Odds Ratio"),
        AttrH("Fisher Strand Bias"),
        AttrH("Allelic Depth", is_seq = True),
        AttrH("Read Depth"),
        AttrH("Genotype Quality"),
    ],
    "view_gnomAD": [
        AttrH("Allele"),
        AttrH("Proband"),
        AttrH("pLI", is_seq = True),
        AttrH("Proband AF", "expert"),
        AttrH("Genome AF"),
        AttrH("Exome AF"),
        AttrH("URL", kind = "link"),
        AttrH("PopMax #1", "expert"),
        AttrH("PopMax #2", "expert"),
    ],
    "view_db": [
        AttrH("HGMD"),
        AttrH("HGMD (HG38)"),
        AttrH("HGMD TAGs", is_seq = True),
        AttrH("HGMD Phenotypes", is_seq = True),
        AttrH("HGMD PMIDs", is_seq = True, kind = "link"),
        AttrH("OMIM", is_seq=True, kind="link"),
        AttrH("ClinVar Significance", is_seq = True),
        AttrH("ClinVar", "link"),
        AttrH("GeneCards", kind="link", is_seq=True),
    ],
    "view_pred": [
        AttrH("LoF Score", is_seq = True),
        AttrH("LoF Score (Canonical)", is_seq = True),
        AttrH("MaxEntScan", is_seq = True),
        AttrH("Polyphen", is_seq = True),
        AttrH("Polyphen 2 HVAR", is_seq = True),
        AttrH("Polyphen 2 HDIV", is_seq = True),
        AttrH("SIFT", is_seq = True),
        AttrH("REVEL", is_seq = True),
        AttrH("Mutation Taster", is_seq = True),
        AttrH("FATHMM", is_seq = True),
        AttrH("CADD (Phred)", is_seq = True),
        AttrH("CADD (Raw)", is_seq = True),
        AttrH("Mutation Assessor", is_seq = True),
        AttrH("SIFT score", is_seq = True),
        AttrH("Polyphen 2 HVAR score", is_seq = True),
        AttrH("Polyphen 2 HDIV score", is_seq = True),
    ],
    "view_genetics": [
        AttrH("Zygosity"),
        AttrH("Inherited from"),
        AttrH("Distance From Intron/Exon Boundary (Worst)", is_seq = True),
        AttrH("Distance From Intron/Exon Boundary (Canonical)", is_seq = True),
        AttrH("Conservation", is_seq = True),
        AttrH("Species with variant"),
        AttrH("Species with other variants"),
        AttrH("MaxEntScan", is_seq=True),
        AttrH("NNSplice"),
        AttrH("Human Splicing Finder"),
        AttrH("other_genes",
            title="Gene symbols from other transcripts", is_seq = True),
        AttrH("Called by", is_seq=True),
        AttrH("CALLER DATA"),
    ],
    "_main": [
        AttrH("label"),
        AttrH("color_code"),
        AttrH("id"),
        AttrH("assembly_name", title = "Assembly"),
        AttrH("seq_region_name"),
        AttrH("start"),
        AttrH("end"),
        AttrH("strand"),
        AttrH("allele_string"),
        AttrH("variant_class"),
        AttrH("most_severe_consequence"),
        AttrH("ClinVar"),
        AttrH("HGMD"),
        AttrH("HGMD_HG38"),
        AttrH("HGMD_PIMIDs", "hidden", is_seq = True),
        AttrH("HGMD_phenotypes", "hidden", is_seq = True),
        AttrH("EXPECTED"),
        AttrH("gnomad_db_genomes_af", "hidden"),
        AttrH("gnomad_db_exomes_af", "hidden"),
        AttrH("SEQaBOO"),
    ],
    "transcripts": [
        AttrH("amino_acids"),
        AttrH("bam_edit"),
        AttrH("biotype"),
        AttrH("cadd_phred"),
        AttrH("cadd_raw"),
        AttrH("canonical"),
        AttrH("ccds"),
        AttrH("cdna_end"),
        AttrH("cdna_start"),
        AttrH("cds_end"),
        AttrH("cds_start"),
        AttrH("clinvar_clnsig"),
        AttrH("clinvar_rs"),
        AttrH("codons"),
        AttrH("consequence_terms", is_seq = True),
        AttrH("conservation"),
        AttrH("distance"),
        AttrH("domains", "json"),
        AttrH("exacpli"),
        AttrH("exon"),
        AttrH("fathmm_pred"),
        AttrH("fathmm_score"),
        AttrH("flags", is_seq = True),
        AttrH("gene_id"),
        AttrH("gene_pheno"),
        AttrH("genesplicer"),
        AttrH("gene_symbol"),
        AttrH("gene_symbol_source"),
        AttrH("given_ref"),
        AttrH("gnomad_exomes_ac"),
        AttrH("gnomad_exomes_af"),
        AttrH("gnomad_exomes_an"),
        AttrH("gnomad_exomes_asj_af"),
        AttrH("gnomad_genomes_ac"),
        AttrH("gnomad_genomes_af"),
        AttrH("gnomad_genomes_an"),
        AttrH("gnomad_genomes_asj_af"),
        AttrH("hgnc_id"),
        AttrH("hgvs_offset"),
        AttrH("hgvsc"),
        AttrH("hgvsp"),
        AttrH("high_inf_pos"),
        AttrH("impact"),
        AttrH("intron"),
        AttrH("loftool"),
        AttrH("maxentscan_alt"),
        AttrH("maxentscan_diff"),
        AttrH("maxentscan_ref"),
        AttrH("motif_feature_id"),
        AttrH("motif_name"),
        AttrH("motif_pos"),
        AttrH("motif_score_change"),
        AttrH("mutationassessor_pred"),
        AttrH("mutationassessor_score"),
        AttrH("mutationtaster_pred"),
        AttrH("mutationtaster_score"),
        AttrH("polyphen2_hdiv_pred"),
        AttrH("polyphen2_hdiv_score"),
        AttrH("polyphen2_hvar_pred"),
        AttrH("polyphen2_hvar_score"),
        AttrH("polyphen_prediction"),
        AttrH("polyphen_score"),
        AttrH("protein_end"),
        AttrH("protein_id"),
        AttrH("protein_start"),
        AttrH("regulatory_feature_id"),
        AttrH("revel_score"),
        AttrH("sift_pred"),
        AttrH("sift_prediction"),
        AttrH("sift_score"),
        AttrH("strand"),
        AttrH("source"),
        AttrH("spliceregion", is_seq = True),
        AttrH("swissprot", is_seq = True),
        AttrH("transcript_id"),
        AttrH("trembl", is_seq = True),
        AttrH("uniparc", is_seq = True),
        AttrH("used_ref"),
        AttrH("variant_allele"),
    ],
    "colocated_v": [
        AttrH("id"),
        AttrH("start"),
        AttrH("end"),
        AttrH("allele_string"),
        AttrH("strand"),
        AttrH("pubmed", is_seq = True),
        AttrH("somatic"),
        AttrH("AA"),
        AttrH("AFR"),
        AttrH("AMR"),
        AttrH("EA"),
        AttrH("EAS"),
        AttrH("EUR"),
        AttrH("SAS"),
        AttrH("frequencies", "json"),
        AttrH("phenotype_or_disease"),
        AttrH("seq_region_name"),
        AttrH("clin_sig", is_seq = True),
        AttrH("minor", attrs = ["minor_allele", "minor_allele_freq"]),
    ]
}

#===============================================
def setupRecommended():
    for aspect_name, attrs in CONFIG_ATTRS.items():
        ViewSetup.setRecomendedAttributes(aspect_name, attrs)
