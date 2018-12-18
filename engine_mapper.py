from crawlers import concordia_engine, uqam_engine, udm_engine, mcgill_engine

engine_map = {
    'concordia': concordia_engine.crawl,
    'uqam' : uqam_engine.crawl,
    'udm': udm_engine.crawl,
    'mcgill': mcgill_engine.crawl
}

