#===============================================
class AnfisaConfig:
    sTextMessages = {
        "aspect.tags.title": "Tags&nbsp;&amp;<br/>Filters"}

    sConfigOptions = {
        "aspect.tags.name": "tags_data",
        # "zones":            [
        #     ("Chromosome", "Chromosome"),
        #     ("Gene",       "Genes"),
        #     ("Tag",        "_tags")],
        "zones":[
            ("Gene",       "Genes"),
            ("Sample",       "Has_Variant"),
            ("Tag", "_tags")
        ],
        "check.tags":       [
            "Previously categorized",
            "Previously Triaged",
            "Not categorized",
            "Benign/Likely benign",
            "False positives"
        ],
        "zygosity.cases": {
            "homo_recess": "Homozygous Recessive",
            "x_linked": "X-linked",
            "dominant": "Autosomal Dominant",
            "compens": "Compensational"
        },
        "rand.min.size":    100,
        "rand.sample.size": 100,

        "max.ws.size":  5000,
        "report.lines": 100,
        "max.export.size": 300,

        "filter.std.mark": u"\u23da",

        "comp-hets.setup": {
            "zygosity": "Custom",
            "Genes": "Genes",
            "Compound_heterozygous": "Compound_heterozygous",
            "ws_compound_heterosygotes": "ws_compound_heterosygotes"
        },

        "job.pool.size":    3,
        "job.pool.threads": 1}

    sTextDecor = {
        "VEP Data": "VEP<br/>Data",
        "VEP Transcripts": "VEP<br/>Transcripts",
        "Colocated Variants": "Colocated<br/>Variants"}

    @classmethod
    def textMessage(cls, key):
        return cls.sTextMessages[key]

    @classmethod
    def configOption(cls, key):
        return cls.sConfigOptions[key]

    @classmethod
    def decorText(cls, text):
        return cls.sTextDecor.get(text, text)

    @classmethod
    def normalizeColorCode(cls, color_code):
        if color_code in {"red", "red-cross",
                "yellow", "yellow-cross", "green"}:
            return color_code
        return "grey"

    @classmethod
    def normalizeTime(cls, time_label):
        if time_label is None:
            return '2019-03-01T00:00:00'
        return time_label

#===============================================
