from Engines import concordia_engine, udm_engine, uqam_engine

engine_map = {
    'concordia': concordia_engine.crawl,
    'uqam' : uqam_engine.crawl
}