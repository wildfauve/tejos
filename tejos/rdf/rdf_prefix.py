from rdflib import Namespace

__clo_te_ns = "https://clojos.io/ontology/FantasyTennis/"
__clo_ind_ns = "https://clojos.io/ontology/FantasyTennis/Ind/"

owl = Namespace("http://www.w3.org/2002/07/owl#")
skos = Namespace('http://www.w3.org/2004/02/skos/core#')

clo_te = Namespace(__clo_te_ns)

clo_te_ind = Namespace(__clo_ind_ns)

clo_te_plr = Namespace(f"{__clo_te_ns}Player/")

clo_te_ind_plr = Namespace(f"{__clo_ind_ns}Player/")

clo_te_ind_tou = Namespace(f"{__clo_ind_ns}Tournament/")

foaf = Namespace("http://xmlns.com/foaf/0.1/")

dcterms = Namespace("http://purl.org/dc/terms/")
