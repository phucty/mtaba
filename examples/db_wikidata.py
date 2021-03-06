# Import class
from core.databases.db_wd import DBWikidata
from config import config as cf

# Wikidb
db = DBWikidata()

### 1. Get Entity Information

# Get label of Belgium (Q31)
print(db.get_label("Q31"))

# Gel label in all languages of Belgium (Q31)
print(db.get_labels("Q31"))
# Get label in a specific language
print(db.get_labels("Q31", "ja"))

# Gel aliases in all languages of Belgium (Q31)
print(db.get_aliases("Q31"))
# Get aliases in a specific language of Belgium (Q31)
print(db.get_aliases("Q31", "ja"))

# Gel descriptions in all languages of Belgium (Q31)
print(db.get_descriptions("Q31"))
# Get descriptions in a specific language of Belgium (Q31)
print(db.get_descriptions("Q31", "ja"))

# Gel sitelinks of Belgium (Q31)
print(db.get_sitelinks("Q31"))

# Gel Wikipedia title of Belgium (Q31)
print(db.get_wikipedia_title("ja", "Q31"))
# Gel Wikipedia link of Belgium (Q31)
print(db.get_wikipedia_link("ja", "Q31"))

# Gel claims of Belgium (Q31)
print(db.get_claims("Q31"))

# Get all information of Belgium (Q31)
print(db.get_item("Q31"))

# Get redirect of Belgium (Q31)
redirects = db.get_redirect_of("Q31")
print(redirects)

# Get redirect of
print(db.get_redirect(redirects[0]))

# Get instance of Belgium (Q31)
instance_ofs = db.get_instance_of("Q31")
for i, wd_id in enumerate(instance_ofs):
    print(f"{i}: {wd_id} - {db.get_label(wd_id)}")

# Get subclass of Belgium (Q31)
print(db.get_subclass_of("Q31"))

# Get all types of Belgium (Q31)
types = db.get_all_types("Q31")
for i, wd_id in enumerate(types):
    print(f"{i}: {wd_id} - {db.get_label(wd_id)}")

### 3. Entities boolean search
# Find subset of entities (head entities) with information about tail entities and properties (triples: <head entities, property, tail entities>)

import time
from config import config as cf


def find_wikidata_items_haswbstatements(params, print_top=3, get_qid=True):
    start = time.time()
    wd_ids = db.get_haswbstatements(params, get_qid=get_qid)
    end = time.time() - start
    print("Query:")
    for logic, prop, qid in params:
        if prop is None:
            prop_label = ""
        else:
            prop_label = f" - {prop}[{db.get_label(prop)}]"

        qid_label = db.get_label(qid)
        print(f"{logic}{prop_label}- {qid}[{qid_label}]")

    print(f"Answers: Found {len(wd_ids):,} items in {end:.5f}s")
    for i, wd_id in enumerate(wd_ids[:print_top]):
        print(f"{i + 1}. {wd_id} - {db.get_label(wd_id)}")
    print(f"{4}. ...")
    print()


print("1.1. Get all female (Q6581072)")
find_wikidata_items_haswbstatements([[cf.ATTR_OPTS.AND, None, "Q6581072"]])

print("1.1. Get all female (Q6581072)")
find_wikidata_items_haswbstatements(
    [[cf.ATTR_OPTS.AND, None, "Q6581072"]], get_qid=False
)

print("1.2. Get all male (Q6581072)")
find_wikidata_items_haswbstatements([[cf.ATTR_OPTS.AND, None, "Q6581097"]])

print("1.2. Get all male (Q6581072)")
find_wikidata_items_haswbstatements(
    [[cf.ATTR_OPTS.AND, None, "Q6581097"]], get_qid=False
)

print(
    "2. Get all entities has relation with Graduate University for Advanced Studies (Q2983844)"
)
find_wikidata_items_haswbstatements(
    [
        # ??? - Graduate University for Advanced Studies
        [cf.ATTR_OPTS.AND, None, "Q2983844"]
    ]
)

print(
    "3. Get all entities who are human, male, educated at Todai, and work at SOKENDAI"
)
find_wikidata_items_haswbstatements(
    [
        # instance of - human
        [cf.ATTR_OPTS.AND, "P31", "Q5"],
        # gender - male
        [cf.ATTR_OPTS.AND, "P21", "Q6581097"],
        # educated at - Todai
        [cf.ATTR_OPTS.AND, "P69", "Q7842"],
        # employer - Graduate University for Advanced Studies
        [cf.ATTR_OPTS.AND, "P108", "Q2983844"],
    ]
)

print("4. Get all entities that have relation with human, male, Todai, and SOKENDAI")
find_wikidata_items_haswbstatements(
    [
        # instance of - human
        [cf.ATTR_OPTS.AND, None, "Q5"],
        # gender - male
        [cf.ATTR_OPTS.AND, None, "Q6581097"],
        # educated at - Todai
        [cf.ATTR_OPTS.AND, None, "Q7842"],
        # employer - Graduate University for Advanced Studies
        [cf.ATTR_OPTS.AND, None, "Q2983844"],
    ]
)

print(
    "5. Get all entities that have relation with scholarly article or DNA, X-ray diffraction, and Francis Crick and Nature"
)
find_wikidata_items_haswbstatements(
    [
        # ? - scholarly article
        [cf.ATTR_OPTS.AND, None, "Q13442814"],
        # ? - DNA
        [cf.ATTR_OPTS.OR, None, "Q7430"],
        # ? - X-ray diffraction
        [cf.ATTR_OPTS.OR, None, "Q12101244"],
        # ? - DNA
        [cf.ATTR_OPTS.OR, None, "Q911331"],
        # Francis Crick
        [cf.ATTR_OPTS.AND, None, "Q123280"],
        # ? - Nature
        [cf.ATTR_OPTS.AND, None, "Q180445"],
    ]
)
