from typing import Callable
from textwrap import dedent
from rdflib import Literal
from rdflib.plugins.sparql.processor import SPARQLResult

from tejos.util import logger



def sparql_prefixes():
    return dedent("""prefix clo-te: <https://clojos.io/ontology/FantasyTennis/>
    prefix clo-te-plr: <https://clojos.io/ontology/FantasyTennis/Player/>
    prefix clo-te-tou: <https://clojos.io/ontology/FantasyTennis/Tournament/>
    prefix clo-te-fan: <https://clojos.io/ontology/FantasyTennis/Fantasy/>
    prefix clo-te-ind: <https://clojos.io/ontology/FantasyTennis/Ind/>
    prefix foaf: <http://xmlns.com/foaf/0.1/>
    prefix skos: <http://www.w3.org/2004/02/skos/core#>
    prefix foaf: <http://xmlns.com/foaf/0.1/>
    """)

def query(g, query_exp: str, prefixes_fn: Callable = sparql_prefixes) -> SPARQLResult:
    logger.log(f"{prefixes_fn()}\n{query_exp}")
    return g.query(f"{prefixes_fn()}\n{query_exp}")


