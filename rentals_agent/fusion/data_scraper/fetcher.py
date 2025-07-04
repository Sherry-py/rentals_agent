import requests
import logging
import time
import random

logger = logging.getLogger(__name__)

def fetch_html(url: str, timeout: int = 10) -> str:
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
        'Referer': 'https://www.realestate.com.au/',
        'Cookie': (
            "CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; "
            "DM_SitId1464=1; DM_SitId1464SecId12707=1; "pip install selenium
            "QSI_HistorySession=https%3A%2F%2Fwww.realestate.com.au%2F~1751531937299; "
            "s_cc=true; ab.storage.sessionId.746d0d98-0c96-45e9-82e3-9dfa6ee28794=%7B%22g%22%3A%2278cebc42-80ff-7ef1-6944-87223b3233a5%22%2C%22e%22%3A1751533864707%2C%22c%22%3A1751530039515%2C%22l%22%3A1751532064707%7D; "
            "nol_fpid=zjfwhbx49uexuvn6nxxlaf20modfj1749202329|1749202329698|1751532064730|1751532064956; "
            "_ga_3J0XCBB972=GS2.1.s1751530041$o7$g1$t1751532066$j54$l0$h0; "
            "KFC=oWmLvYxgy07hQF/ZNdYV9HS3DZPpHHFX/33zoRnrZgc=|1751532174328; "
            "KP_UIDz-ssn=0HAudk0HbXXCHDOrOJHIKqEGwKTUUW6MTmOkEOCOYgWz3GpzfnPZJ6r5KQ7A7qKjg4V7HEr7oD2Tj2aiRDo0UREqmC1BXkfYABM89lFj7tjMeDwIVEcCN14mqkVo1vcCRLqjYvK5AsAPl3N1RhUK44vTXAfMLI4nPM1l09GM; "
            "KP_UIDz=0HAudk0HbXXCHDOrOJHIK"
        )
    }