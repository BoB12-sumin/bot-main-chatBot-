from splunklib.searchcommands import dispatch, GeneratingCommand, Option, Configuration
import virustotal3.core
from config import virus_total_api_key as api_key


def virustotal(query_item, query_type):
    """ virustotal api """
    if query_type == 'ip':
        virus_total = virustotal3.core.IP(api_key)
    elif query_type == 'domain':
        virus_total = virustotal3.core.Domains(api_key)
    elif query_type == 'url':
        virus_total = virustotal3.core.URL(api_key)