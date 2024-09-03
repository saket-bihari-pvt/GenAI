import logging
import os
import pickle
from sentence_transformers import SentenceTransformer
import re

# get package root directory
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def generate_embeddings(emb_path: str, save_emb: bool = True) -> tuple[dict, dict]:
    """
    For each db, generate embeddings for all of the column names and descriptions
    """
    encoder = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2", device="cpu"
    )
    emb = {}
    csv_descriptions = {}
    glossary_emb = {}
    with open('/home/ubuntu/metadata.sql') as f:
        lines = f.readlines()
    lines_lcase = [x.lower().strip() for x in lines]
    varcharpattern = r'varchar2\(\d+\)'
    tablename =""
    db_name = "ttech"
    column_descriptions = []
    column_descriptions_typed = []

    for i in lines_lcase:
        if i.startswith('--') or len(i) == 0 or i.startswith(');'):
            continue
        if i.startswith('create') :
            words = i.split()
            tablename = words[2]
            #print(tablename)
        else:
            if ',' in i:
               parts = i.split(',')
               column_name, data_type = parts[0].split()
               data_type = re.sub(varcharpattern, 'text', data_type).replace('number','bigint')
               column_description = parts[1].strip().lstrip('--').rstrip('.')
               #print(tablename+'.' + column_name +',' + data_type + ',' + column_description)
            else:
                index_of_dash = i.find("--")
                column_name, data_type = i[:index_of_dash].split()
                data_type = re.sub(varcharpattern, 'text', data_type)
                column_description = i[index_of_dash:].lstrip('- ').rstrip('.').replace('number','bigint')
                #print(tablename+'.' + column_name +',' + data_type + ',' + column_description)
            col_str = (
                tablename
                + "."
                + column_name
                + ": "
                + column_description
            )
            col_str_typed = (
                tablename
                + "."
                + column_name
                + ","
                + data_type
                + ","
                + column_description
            )
            column_descriptions.append(col_str)
            column_descriptions_typed.append(col_str_typed)
        column_emb = encoder.encode(column_descriptions, convert_to_tensor=True)
        emb[db_name] = column_emb
        csv_descriptions[db_name] = column_descriptions_typed
        glossary = []
        if len(glossary) > 0:
            glossary_embeddings = encoder.encode(glossary, convert_to_tensor=True)
        else:
            glossary_embeddings = []
        glossary_emb[db_name] = glossary_embeddings
    if save_emb:
        # get directory of emb_path and create if it doesn't exist
        emb_dir = os.path.dirname(emb_path)
        if not os.path.exists(emb_dir):
            os.makedirs(emb_dir)
        with open(emb_path, "wb") as f:
            pickle.dump((emb, csv_descriptions, glossary_emb), f)
            logging.info(f"Saved embeddings to file {emb_path}")
    return emb, csv_descriptions, glossary_emb

def clean_glossary(glossary: str) -> list[str]:
    """
    Clean glossary by removing number bullets and periods, and making sure every line starts with a dash bullet.
    """
    if glossary == "":
        return []
    glossary = glossary.split("\n")
    # remove empty strings
    glossary = list(filter(None, glossary))
    cleaned = []
    for line in glossary:
        # remove number bullets and periods
        line = re.sub(r"^\d+\.?\s?", "", line)
        # make sure every line starts with a dash bullet if it does not already
        line = re.sub(r"^(?!-)", "- ", line)
        cleaned.append(line)
    glossary = cleaned
    return glossary

def load_embeddings(emb_path: str) -> tuple[dict, dict]:
    """
    Load embeddings from file if they exist, otherwise generate them and save them.
    """
    if os.path.isfile(emb_path):
        logging.info(f"Loading embeddings from file {emb_path}")
        with open(emb_path, "rb") as f:
            emb, csv_descriptions, glossary_emb = pickle.load(f)
        return emb, csv_descriptions, glossary_emb
    else:
        logging.info(f"Embeddings file {emb_path} does not exist.")
        emb, csv_descriptions, glossary_emb = generate_embeddings(emb_path)
        return emb, csv_descriptions, glossary_emb


# entity types: list of (column, type, description) tuples
# note that these are spacy types https://spacy.io/usage/linguistic-features#named-entities
# we can add more types if we want, but PERSON, GPE, ORG should be
# sufficient for most use cases.
# also note that DATE and TIME are not included because they are usually
# retrievable from the top k embedding search due to the limited list of nouns
columns_ner = {
    "ttech": {
        "PERSON": [
            "finance_summary_data.biller,text,person responsible for issuing invoices",
            "finance_summary_data.program_mgr,text,program manager",
            "finance_summary_data.project_mgr,text,project manager",
            "finance_summary_data.ops_mgr,text,manager responsible for operations",
            "finance_summary_data.sr_project_team,text,senior project team members",
            "finance_summary_data.contract_admin,text,contract administrator",
        ],
        "ORG": [
            "finance_summary_data.company_id,text,company id",
            "company_lkp.company_id,text,company id",
            "company_lkp.company_name,text,company name",
            "finance_summary_data.company,text,company name",
            "finance_summary_data.entity_id,bigint,unique id for business entities within the company",
            "finance_summary_data.group_id,bigint,unique code for groups within the company",
            "finance_summary_data.business_group,text,business group code",
            "finance_summary_data.division,text,division code",
            "finance_summary_data.cl_op_grp,text,focuses on client services and interactions",
            "finance_summary_data.project_id,bigint,unique identifier for a specific project",
            "finance_summary_data.project_num,text,project number",
            "finance_summary_data.acct_ctr,text,account center",
            "finance_summary_data.acct_grp,text,account group",
            "finance_summary_data.parent_customer_number,bigint,number for the parent customer",
            "finance_summary_data.parent_customer_name,text,name of the parent customer",
            "finance_summary_data.end_parent_customer_number,bigint,number for the end parent customer",
            "finance_summary_data.end_parent_customer_name,text,name of the end parent customer",
            "finance_summary_data.operations_group,text,operations group",
            "finance_summary_data.end_customer_code,text,end customer code",
            "finance_summary_data.end_customer_type,text,end customer type",
            "finance_summary_data.end_customer_name,text,name of the end customer",
            "finance_summary_data.end_customer_num,bigint,end customer number",
            "finance_summary_data.programs,text,program name",
        ],
        "MONEY": [
            "finance_summary_data.itd_tot_rev,bigint,total revenue inception to date",
            "finance_summary_data.itd_net_rev,bigint,net revenue inception to date",
            "finance_summary_data.itd_tot_brdn_cst,bigint,total burden costs from project inception",
            "finance_summary_data.itd_tot_prft,bigint,total profit from project inception to date",
            "finance_summary_data.cur_tot_cst_bgt,bigint,current total cost budget",
            "finance_summary_data.cur_tot_rev_bgt,bigint,current total revenue budget",
            "finance_summary_data.cur_eac_prft,bigint,current estimate at completion profit",
            "finance_summary_data.cur_eac_prft_percent,bigint,current estimate at completion profit percentage",
            "finance_summary_data.org_tot_cst_bgt,bigint,original total cost budget",
            "finance_summary_data.org_tot_rev_bgt,bigint,original total revenue budget",
            "finance_summary_data.org_eac_prft,bigint,original estimate at completion profit",
            "finance_summary_data.ptd_lbr_rev,bigint,period-to-date labor revenue",
            "finance_summary_data.ptd_odc_rev,bigint,period-to-date other direct costs revenue",
            "finance_summary_data.ptd_sub_rev,bigint,period-to-date subcontractor revenue",
            "finance_summary_data.ptd_tot_rev,bigint,period-to-date total revenue",
            "finance_summary_data.ptd_net_rev,bigint,period-to-date net revenue",
            "finance_summary_data.ptd_lbr_cst,bigint,period-to-date labor cost",
            "finance_summary_data.ptd_odc_cst,bigint,period-to-date other direct costs",
            "finance_summary_data.ptd_sub_cst,bigint,period-to-date subcontractor cost",
            "finance_summary_data.ptd_prov_loss,bigint,period-to-date provisional loss",
            "finance_summary_data.ptd_brdn_cst,bigint,period-to-date burden cost",
            "finance_summary_data.ptd_tot_brdn_cst,bigint,period-to-date total burden cost",
            "finance_summary_data.ptd_tot_prft,bigint,period-to-date total profit",
            "finance_summary_data.ptd_tot_prft_percent,bigint,period-to-date total profit percentage",
            "finance_summary_data.qtd_lbr_rev,bigint,quarter-to-date labor revenue",
            "finance_summary_data.qtd_odc_rev,bigint,quarter-to-date other direct costs revenue",
            "finance_summary_data.qtd_sub_rev,bigint,quarter-to-date subcontractor revenue",
            "finance_summary_data.qtd_tot_rev,bigint,quarter-to-date total revenue",
            "finance_summary_data.qtd_net_rev,bigint,quarter-to-date net revenue",
            "finance_summary_data.qtd_lbr_cst,bigint,quarter-to-date labor cost",
            "finance_summary_data.qtd_odc_cst,bigint,quarter-to-date other direct costs",
            "finance_summary_data.qtd_sub_cst,bigint,quarter-to-date subcontractor cost",
            "finance_summary_data.qtd_prov_loss,bigint,quarter-to-date provisional loss",
            "finance_summary_data.qtd_brdn_cst,bigint,quarter-to-date burden cost",
            "finance_summary_data.qtd_tot_brdn_cst,bigint,quarter-to-date total burden cost",
            "finance_summary_data.qtd_tot_prft,bigint,quarter-to-date total profit",
            "finance_summary_data.ytd_lbr_rev,bigint,year-to-date labor revenue",
            "finance_summary_data.ytd_odc_rev,bigint,year-to-date other direct costs revenue",
            "finance_summary_data.ytd_sub_rev,bigint,year-to-date subcontractor revenue",
            "finance_summary_data.ytd_rev_tot,bigint,year-to-date total revenue",
            "finance_summary_data.ytd_lbr_cst,bigint,year-to-date labor cost",
            "finance_summary_data.ytd_odc_cst,bigint,year-to-date other direct costs",
            "finance_summary_data.ytd_sub_cst,bigint,year-to-date subcontractor cost",
            "finance_summary_data.ytd_prov_loss,bigint,year-to-date provisional loss",
            "finance_summary_data.ytd_brdn_cst,bigint,year-to-date burden cost",
            "finance_summary_data.ytd_tot_brdn_cst,bigint,year-to-date total burden cost",
            "finance_summary_data.ytd_tot_rev,bigint,year-to-date total revenue",
            "finance_summary_data.ytd_net_rev,bigint,year-to-date net revenue",
            "finance_summary_data.ytd_tot_prft,bigint,year-to-date total profit",
            "finance_summary_data.itd_lbr_rev,bigint,inception-to-date labor revenue",
            "finance_summary_data.itd_odc_rev,bigint,inception-to-date other direct costs revenue",
            "finance_summary_data.itd_sub_rev,bigint,inception-to-date subcontractor revenue",
            "finance_summary_data.itd_lbr_cst,bigint,inception-to-date labor cost",
            "finance_summary_data.itd_odc_cst,bigint,inception-to-date other direct costs",
            "finance_summary_data.itd_sub_cst,bigint,inception-to-date subcontractor cost",
            "finance_summary_data.itd_prov_loss,bigint,inception-to-date provisional loss",
            "finance_summary_data.itd_brdn_cst,bigint,inception-to-date burden cost",
            "finance_summary_data.ptd_tot_inv,bigint,period-to-date total invoice",
            "finance_summary_data.qtd_tot_inv,bigint,quarter-to-date total invoice",
            "finance_summary_data.ytd_tot_inv,bigint,year-to-date total invoice",
            "finance_summary_data.itd_tot_inv,bigint,inception-to-date total invoice",
            "finance_summary_data.ptd_funding,bigint,period-to-date funding",
            "finance_summary_data.qtd_funding,bigint,quarter-to-date funding",
            "finance_summary_data.ytd_funding,bigint,year-to-date funding",
            "finance_summary_data.itd_funding,bigint,inception-to-date funding",
            "finance_summary_data.ar_current,bigint,current accounts receivable",
            "finance_summary_data.ar_31_60_days,bigint,accounts receivable 31-60 days old",
            "finance_summary_data.ar_61_90_days,bigint,accounts receivable 61-90 days old",
            "finance_summary_data.ar_91_120_days,bigint,accounts receivable 91-120 days old",
            "finance_summary_data.ar_120plus_days,bigint,accounts receivable over 120 days old",
            "finance_summary_data.ar_balance,bigint,total accounts receivable balance",
            "finance_summary_data.unb_0_30_days,bigint,unbilled revenue 0-30 days",
            "finance_summary_data.unb_31_60_days,bigint,unbilled revenue 31-60 days",
            "finance_summary_data.unb_61_90_days,bigint,unbilled revenue 61-90 days",
            "finance_summary_data.unb_91_120_days,bigint,unbilled revenue 91-120 days",
            "finance_summary_data.unb_120plus_days,bigint,unbilled revenue over 120 days",
            "finance_summary_data.retention,bigint,retained earnings or holdback from payments",
            "finance_summary_data.ptd_bad_debt_wo,bigint,period-to-date bad debt written off",
            "finance_summary_data.ytd_bad_debt_wo,bigint,year-to-date bad debt written off",
            "finance_summary_data.itd_bad_debt_wo,bigint,inception-to-date bad debt written off",
            "finance_summary_data.cash_rcpts_ptd,bigint,period-to-date cash receipts",
            "finance_summary_data.cash_rcpts_qtd,bigint,quarter-to-date cash receipts",
            "finance_summary_data.cash_rcpts_ytd,bigint,year-to-date cash receipts",
            "finance_summary_data.cash_rcpts_itd,bigint,inception-to-date cash receipts",
            "finance_summary_data.wip_balance,bigint,work in progress balance",
            "finance_summary_data.revenue_3mo,bigint,revenue over the last 3 months",
            "finance_summary_data.open_commnts,bigint,open comments regarding financials or projects",
            "finance_summary_data.unbilled,bigint,amount of work completed but not yet billed",
            "finance_summary_data.unearned,bigint,revenue received but not yet earned",
            "finance_summary_data.roll_3mo_rev,bigint,rolling 3-month revenue forecast",
            "finance_summary_data.ap_balance,bigint,accounts payable balance",
            "finance_summary_data.itd_spend,bigint,inception-to-date total spend",
            "finance_summary_data.acr_sub_itd,bigint,inception-to-date accrued subcontractor cost",
            "finance_summary_data.acr_odc_itd,bigint,inception-to-date accrued other direct costs",
            "finance_summary_data.pm_bgt,bigint,project management budget",
            "finance_summary_data.pm_itd,bigint,inception-to-date project management spend",
            "finance_summary_data.projfunc_currency_code,text,currency code for project financials",
            "finance_summary_data.rev_bgt_remaining,bigint,remaining revenue budget",
            "finance_summary_data.cst_bgt_remaining,bigint,remaining cost budget",
            "finance_summary_data.rev_at_risk,bigint,revenue at risk",
            "finance_summary_data.cost_only_at_risk,bigint,cost at risk of not being covered by revenue",
            "finance_summary_data.rev_sought,bigint,additional revenue sought",
            "finance_summary_data.backlog,bigint,work that is scheduled but not yet completed",
            "finance_summary_data.jv_amt_ptd,bigint,period-to-date joint venture amount",
            "finance_summary_data.jv_amt_qtd,bigint,quarter-to-date joint venture amount",
            "finance_summary_data.jv_amt_ytd,bigint,year-to-date joint venture amount",
            "finance_summary_data.jv_amt_itd,bigint,inception-to-date joint venture amount",
            "finance_summary_data.qtd_bad_debt_wo,bigint,quarter-to-date bad debt written off",
            "finance_summary_data.cost_bdn_ovh_itd,bigint,inception-to-date cost for overhead burden",
            "finance_summary_data.cost_bdn_ga_itd,bigint,inception-to-date cost for general and administrative burden",
            "finance_summary_data.cost_bdn_selling_itd,bigint,inception-to-date selling burden cost",
            "finance_summary_data.cost_bdn_efb_itd,bigint,inception-to-date efb (engineering",
            "finance_summary_data.cost_bdn_ovh_ptd,bigint,period-to-date overhead burden cost",
            "finance_summary_data.cost_bdn_ga_ptd,bigint,period-to-date general and administrative burden cost",
            "finance_summary_data.cost_bdn_selling_ptd,bigint,period-to-date selling burden cost",
            "finance_summary_data.cost_bdn_efb_ptd,bigint,period-to-date efb (engineering",
            "finance_summary_data.cost_bdn_ovh_qtd,bigint,quarter-to-date overhead burden cost",
            "finance_summary_data.cost_bdn_ga_qtd,bigint,quarter-to-date general and administrative burden cost",
            "finance_summary_data.cost_bdn_selling_qtd,bigint,quarter-to-date selling burden cost",
            "finance_summary_data.cost_bdn_efb_qtd,bigint,quarter-to-date efb (engineering",
            "finance_summary_data.cost_bdn_ovh_ytd,bigint,year-to-date overhead burden cost",
            "finance_summary_data.cost_bdn_ga_ytd,bigint,year-to-date general and administrative burden cost",
            "finance_summary_data.cost_bdn_selling_ytd,bigint,year-to-date selling burden cost",
            "finance_summary_data.cost_bdn_efb_ytd,bigint,year-to-date efb (engineering",
            "finance_summary_data.open_commitment,bigint,open financial commitments",
            "finance_summary_data.fx_impact,bigint,foeign exchange impact",
            "finance_summary_data.sales_tax_ptd,bigint,period-to-date sales tax",
            "finance_summary_data.sales_tax_qtd,bigint,quarter-to-date sales tax",
            "finance_summary_data.sales_tax_ytd,bigint,year-to-date sales tax",
            "finance_summary_data.sales_tax_itd,bigint,inception-to-date sales tax",
            "finance_summary_data.agreement_amt,bigint,agreement amount",
            "finance_summary_data.proj_distro_rule,text,code for distribution rule for project allocation",
            "finance_summary_data.master_agrmnt_num,text,master agreement number",
            "finance_summary_data.contract_num,text,contract number",
            "finance_summary_data.prime_cont_num,text,prime contract number",
            "finance_summary_data.prime_vs_sub,text,indicator for prime vs subcontractor",
            "finance_summary_data.agreement_num,text,agreement number",
            "finance_summary_data.contract_type,text,type of contract",
            "finance_summary_data.service_type,text,service type",
            "finance_summary_data.facility_function,text,facility function",
            "finance_summary_data.naics,text,naics code",
            "finance_summary_data.inv_limit_flg,text,invoice limit flag",
            "finance_summary_data.project_name,text,name of the project",
            "finance_summary_data.project_type,text,project type",
            "finance_summary_data.public_flg,text,public project flag",
            "finance_summary_data.proj_status,text,current status of the project",
            "finance_summary_data.rev_limit_flg,text,flag for revenue limit",
            "finance_summary_data.sub_initiative,text,sub-initiative",
            "finance_summary_data.project_currency_code,text, project currency code",
            "finance_summary_data.table_type,text,type of table or data structure used for financials",
            "finance_summary_data.initiatives,text,specific initiatives or objectives within the project",
            "finance_summary_data.functional_currency_code,text,currency code",
            "finance_summary_data.description,text,description of the item or category",
        ],
        "DATE": [
            "finance_summary_data.gl_period,text,time period for general ledger entries",
            "finance_summary_data.fiscal_year,bigint,financial year",
            "finance_summary_data.fiscal_month,text,specific month within the fiscal year",
            "finance_summary_data.proj_start_date,date,start date of the project",
            "finance_summary_data.proj_end_date,date,end date of the project",
        ],
        "LOC": [
            "finance_summary_data.project_location,text,location of the project",
            "finance_summary_data.work_location,text,work location",
            "finance_summary_data.locations,text,physical or geographical locations involved",
            "finance_summary_data.proj_mgr_location,text,location of the project manager",
        ],
        "QUANTITY": [
            "finance_summary_data.ptd_lbr_hrs,bigint,period-to-date labor hours",
            "finance_summary_data.qtd_lbr_hrs,bigint,quarter-to-date labor hours",
            "finance_summary_data.ytd_lbr_hrs,bigint,year-to-date labor hours",
            "finance_summary_data.itd_lbr_hrs,bigint,inception-to-date labor hours",
            "finance_summary_data.ptd_activity,bigint,period-to-date activities or tasks completed",
            "finance_summary_data.qtd_activity,bigint,quarter-to-date activities or tasks completed",
            "finance_summary_data.ytd_activity,number,year-to-date activities or tasks completed",
        ],
        "PCT": [
            "finance_summary_data.cst_pct_complete,bigint,percentage of project cost completion",
            "finance_summary_data.qtd_tot_prft_percent,bigint,quarter-to-date total profit percentage",
            "finance_summary_data.ytd_tot_prft_percent,bigint,year-to-date total profit percentage",
            "finance_summary_data.itd_tot_prft_percent,bigint,inception-to-date total profit percentage",
        ],
    },
}
columns_join = {
    "ttech": {
        ("company_lkp" , "finance_summary_data", ): [("company_lkp.company_id" , "finance_summary_data.company_id" )],
    },
}
