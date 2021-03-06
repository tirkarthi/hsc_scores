import json
import bs4
import requests

cookies = {
    'cookie_anonymity_phpsesid': 'b2',
    'ci_session': '5b77',
}

headers = {
    'Origin': 'http://tnea.a4n.in',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Cache-Control': 'max-age=0',
    'Referer': 'http://tnea.a4n.in/home/college_search',
    'Connection': 'keep-alive',
}

caste_codes = ['oc', 'bc', 'bcm', 'mbc', 'sca', 'sc', 'st']

college_codes = {
  "0001",
  "0002",
  "0004",
  "1013",
  "1014",
  "1015",
  "1026",
  "1101",
  "1102",
  "1104",
  "1106",
  "1107",
  "1108",
  "1110",
  "1112",
  "1113",
  "1114",
  "1115",
  "1116",
  "1118",
  "1120",
  "1121",
  "1122",
  "1123",
  "1124",
  "1125",
  "1126",
  "1127",
  "1128",
  "1131",
  "1133",
  "1136",
  "1137",
  "1140",
  "1141",
  "1149",
  "1201",
  "1202",
  "1205",
  "1206",
  "1207",
  "1208",
  "1209",
  "1210",
  "1211",
  "1212",
  "1213",
  "1214",
  "1216",
  "1217",
  "1218",
  "1219",
  "1221",
  "1222",
  "1225",
  "1226",
  "1228",
  "1229",
  "1230",
  "1231",
  "1232",
  "1233",
  "1234",
  "1235",
  "1237",
  "1238",
  "1241",
  "1242",
  "1243",
  "1245",
  "1301",
  "1303",
  "1304",
  "1306",
  "1307",
  "1309",
  "1310",
  "1311",
  "1313",
  "1315",
  "1316",
  "1317",
  "1318",
  "1319",
  "1320",
  "1321",
  "1322",
  "1323",
  "1324",
  "1325",
  "1331",
  "1333",
  "1334",
  "1335",
  "1399",
  "1401",
  "1402",
  "1405",
  "1406",
  "1407",
  "1408",
  "1409",
  "1411",
  "1412",
  "1413",
  "1414",
  "1415",
  "1416",
  "1417",
  "1418",
  "1419",
  "1420",
  "1421",
  "1422",
  "1423",
  "1424",
  "1426",
  "1427",
  "1428",
  "1429",
  "1430",
  "1431",
  "1432",
  "1433",
  "1434",
  "1435",
  "1436",
  "1437",
  "1438",
  "1439",
  "1440",
  "1441",
  "1442",
  "1443",
  "1444",
  "1445",
  "1447",
  "1448",
  "1449",
  "1450",
  "1452",
  "1455",
  "1501",
  "1503",
  "1504",
  "1505",
  "1506",
  "1507",
  "1508",
  "1509",
  "1510",
  "1511",
  "1512",
  "1513",
  "1514",
  "1515",
  "1516",
  "1517",
  "1518",
  "1519",
  "1520",
  "1521",
  "1522",
  "1523",
  "1524",
  "1525",
  "1526",
  "1528",
  "1529",
  "1605",
  "2005",
  "2006",
  "2007",
  "2302",
  "2314",
  "2327",
  "2328",
  "2329",
  "2332",
  "2337",
  "2338",
  "2340",
  "2341",
  "2342",
  "2345",
  "2346",
  "2347",
  "2349",
  "2350",
  "2354",
  "2355",
  "2356",
  "2357",
  "2358",
  "2360",
  "2362",
  "2367",
  "2368",
  "2369",
  "2377",
  "2601",
  "2602",
  "2603",
  "2604",
  "2606",
  "2607",
  "2608",
  "2609",
  "2610",
  "2611",
  "2612",
  "2613",
  "2614",
  "2615",
  "2616",
  "2617",
  "2618",
  "2620",
  "2621",
  "2622",
  "2623",
  "2624",
  "2625",
  "2626",
  "2627",
  "2628",
  "2629",
  "2630",
  "2631",
  "2632",
  "2633",
  "2634",
  "2635",
  "2636",
  "2638",
  "2639",
  "2640",
  "2641",
  "2642",
  "2643",
  "2646",
  "2647",
  "2648",
  "2649",
  "2650",
  "2651",
  "2652",
  "2653",
  "2654",
  "2655",
  "2656",
  "2657",
  "2658",
  "2659",
  "2660",
  "2661",
  "2662",
  "2663",
  "2664",
  "2665",
  "2666",
  "2673",
  "2682",
  "2683",
  "2702",
  "2704",
  "2705",
  "2706",
  "2707",
  "2708",
  "2709",
  "2710",
  "2711",
  "2712",
  "2713",
  "2714",
  "2715",
  "2716",
  "2717",
  "2718",
  "2719",
  "2721",
  "2722",
  "2723",
  "2724",
  "2725",
  "2726",
  "2727",
  "2729",
  "2730",
  "2731",
  "2732",
  "2733",
  "2734",
  "2735",
  "2736",
  "2737",
  "2738",
  "2739",
  "2740",
  "2741",
  "2742",
  "2743",
  "2744",
  "2745",
  "2746",
  "2747",
  "2748",
  "2749",
  "2750",
  "2751",
  "2752",
  "2753",
  "2754",
  "2755",
  "2757",
  "2758",
  "2761",
  "2762",
  "2763",
  "2764",
  "2765",
  "2767",
  "2768",
  "2769",
  "2770",
  "2771",
  "2772",
  "2776",
  "3011",
  "3016",
  "3018",
  "3019",
  "3021",
  "3403",
  "3410",
  "3425",
  "3451",
  "3454",
  "3456",
  "3457",
  "3458",
  "3459",
  "3460",
  "3461",
  "3462",
  "3463",
  "3464",
  "3465",
  "3466",
  "3701",
  "3760",
  "3766",
  "3781",
  "3782",
  "3786",
  "3795",
  "3801",
  "3802",
  "3803",
  "3804",
  "3805",
  "3806",
  "3807",
  "3808",
  "3809",
  "3810",
  "3811",
  "3812",
  "3813",
  "3814",
  "3815",
  "3817",
  "3819",
  "3820",
  "3821",
  "3822",
  "3823",
  "3825",
  "3826",
  "3828",
  "3829",
  "3830",
  "3831",
  "3833",
  "3841",
  "3843",
  "3844",
  "3845",
  "3846",
  "3847",
  "3848",
  "3849",
  "3850",
  "3852",
  "3853",
  "3854",
  "3855",
  "3856",
  "3857",
  "3859",
  "3860",
  "3905",
  "3908",
  "3918",
  "3920",
  "3923",
  "3925",
  "3926",
  "4023",
  "4024",
  "4669",
  "4670",
  "4672",
  "4675",
  "4676",
  "4677",
  "4678",
  "4680",
  "4864",
  "4917",
  "4927",
  "4928",
  "4929",
  "4931",
  "4932",
  "4933",
  "4934",
  "4937",
  "4938",
  "4941",
  "4943",
  "4944",
  "4945",
  "4946",
  "4948",
  "4949",
  "4950",
  "4952",
  "4953",
  "4954",
  "4955",
  "4956",
  "4957",
  "4958",
  "4959",
  "4960",
  "4961",
  "4962",
  "4964",
  "4965",
  "4966",
  "4967",
  "4968",
  "4969",
  "4970",
  "4971",
  "4972",
  "4973",
  "4974",
  "4975",
  "4976",
  "4977",
  "4978",
  "4979",
  "4980",
  "4981",
  "4982",
  "4983",
  "4984",
  "4985",
  "4987",
  "4989",
  "4991",
  "4992",
  "4993",
  "4994",
  "4995",
  "4996",
  "4998",
  "4999",
  "5008",
  "5009",
  "5012",
  "5017",
  "5022",
  "5502",
  "5530",
  "5531",
  "5532",
  "5533",
  "5535",
  "5536",
  "5537",
  "5540",
  "5703",
  "5720",
  "5832",
  "5842",
  "5851",
  "5862",
  "5865",
  "5901",
  "5902",
  "5903",
  "5904",
  "5907",
  "5909",
  "5910",
  "5911",
  "5912",
  "5913",
  "5914",
  "5915",
  "5916",
  "5919",
  "5921",
  "5922",
  "5924",
  "5930",
  "5935",
  "5942",
  "5986",
  "5988",
  "5990",
  "2636",
  "5901",
  "1323",
  "1441",
  "4937",
  "1436",
  "3821",
  "2604",
  "3801",
  "4680",
  "1101",
  "1233",
  "1501",
  "1401",
  "2601",
  "2744",
  "1316",
  "2332",
  "2763",
  "1331",
  "2652",
  "1228",
  "1303",
  "2733",
  "3803",
  "3849",
  "2602",
  "1137",
  "1402",
  "4999",
  "1133",
  "1524",
  "2648",
  "1230",
  "1455",
  "3804",
  "1201",
  "5540",
  "3462",
  "2367",
  "1232",
  "1334",
  "1503",
  "2356",
  "4944",
  "1508",
  "1504",
  "3855",
  "1423",
  "2338",
  "2347",
  "1435",
  "2702",
  "4992",
  "1102",
  "5902",
  "1519",
  "2643",
  "2772",
  "1505",
  "3841",
  "3425",
  "5531",
  "4952",
  "4953",
  "3828",
  "5012",
  "1321",
  "4931",
  "3926",
  "1444",
  "1399",
  "2355",
  "2630",
  "2650",
  "5703",
  "2635",
  "2704",
  "2007",
  "2705",
  "1202",
  "1424",
  "2349",
  "1405",
  "2743",
  "3457",
  "1322",
  "3805",
  "3458",
  "3459",
  "2345",
  "4946",
  "4975",
  "2706",
  "2736",
  "2662",
  "2771",
  "3822",
  "1406",
  "4954",
  "3806",
  "1428",
  "2749",
  "1304",
  "4980",
  "3463",
  "2621",
  "2656",
  "2707",
  "2664",
  "2634",
  "5935",
  "4955",
  "1506",
  "1407",
  "1507",
  "5924",
  "2341",
  "1523",
  "2660",
  "2624",
  "1123",
  "1429",
  "2603",
  "2369",
  "2615",
  "3465",
  "3464",
  "4974",
  "5009",
  "2005",
  "1238",
  "3461",
  "2708",
  "2740",
  "4934",
  "2362",
  "1605",
  "1408",
  "3845",
  "4932",
  "1234",
  "1229",
  "3831",
  "4976",
  "2732",
  "2709",
  "2769",
  "1235",
  "2758",
  "4994",
  "3807",
  "2647",
  "5537",
  "2350",
  "4987",
  "2762",
  "1447",
  "2651",
  "1221",
  "1106",
  "1107",
  "1416",
  "1440",
  "2640",
  "2606",
  "4956",
  "4957",
  "3808",
  "1306",
  "1140",
  "1206",
  "1320",
  "1307",
  "1126",
  "4958",
  "1245",
  "4985",
  "2764",
  "2328",
  "3830",
  "3701",
  "1311",
  "3781",
  "5904",
  "5903",
  "3456",
  "2613",
  "2607",
  "2770",
  "4991",
  "4959",
  "1208",
  "1409",
  "2710",
  "2735",
  "2649",
  "2745",
  "2751",
  "2631",
  "3905",
  "1207",
  "1520",
  "5533",
  "2750",
  "2653",
  "2711",
  "3826",
  "3410",
  "1528",
  "2746",
  "2712",
  "3809",
  "5990",
  "1443",
  "4983",
  "1205",
  "4677",
  "1450",
  "1225",
  "4993",
  "3843",
  "2608",
  "3810",
  "3829",
  "3786",
  "3925",
  "4929",
  "3811",
  "2713",
  "1411",
  "1243",
  "5842",
  "1108",
  "1430",
  "4998",
  "3403",
  "2714",
  "2742",
  "2730",
  "2724",
  "3854",
  "2623",
  "2609",
  "2638",
  "2665",
  "2632",
  "1412",
  "5536",
  "4928",
  "4927",
  "4984",
  "1509",
  "3857",
  "1309",
  "4960",
  "1310",
  "3923",
  "1301",
  "5907",
  "3812",
  "3846",
  "3908",
  "2314",
  "2610",
  "5832",
  "2327",
  "5865",
  "2752",
  "2715",
  "2639",
  "4977",
  "4961",
  "4962",
  "2729",
  "2755",
  "3466",
  "1431",
  "3782",
  "5909",
  "1529",
  "3813",
  "2741",
  "2612",
  "1222",
  "3814",
  "2006",
  "4965",
  "4995",
  "2642",
  "1226",
  "5911",
  "2628",
  "2611",
  "1104",
  "1209",
  "5912",
  "1210",
  "1231",
  "5916",
  "3833",
  "2716",
  "2768",
  "2657",
  "3815",
  "3856",
  "1452",
  "4966",
  "1125",
  "1525",
  "2354",
  "4981",
  "2753",
  "1110",
  "1442",
  "1414",
  "1510",
  "2682",
  "2377",
  "4964",
  "4989",
  "4949",
  "5910",
  "2731",
  "1112",
  "1128",
  "1113",
  "5913",
  "1141",
  "5862",
  "5914",
  "1211",
  "1432",
  "4973",
  "4948",
  "1212",
  "4678",
  "2737",
  "1511",
  "2329",
  "4676",
  "3847",
  "3817",
  "4670",
  "1437",
  "2776",
  "2734",
  "2663",
  "2654",
  "4967",
  "1114",
  "1512",
  "1522",
  "1213",
  "1439",
  "2614",
  "5915",
  "1214",
  "2659",
  "1124",
  "2616",
  "3819",
  "1515",
  "1449",
  "4968",
  "2738",
  "2717",
  "4943",
  "1216",
  "5930",
  "4969",
  "2358",
  "2627",
  "3859",
  "2629",
  "2617",
  "4917",
  "3918",
  "3853",
  "3844",
  "2346",
  "2747",
  "2683",
  "1417",
  "3802",
  "1521",
  "3760",
  "4938",
  "1313",
  "3451",
  "2726",
  "2618",
  "1438",
  "2673",
  "1242",
  "1217",
  "4970",
  "2767",
  "1433",
  "1513",
  "3852",
  "2739",
  "1526",
  "2718",
  "2722",
  "1427",
  "1335",
  "1418",
  "1218",
  "1514",
  "5502",
  "3454",
  "2719",
  "2725",
  "1448",
  "2754",
  "1426",
  "2342",
  "1445",
  "1324",
  "1419",
  "2727",
  "2302",
  "1315",
  "5720",
  "2340",
  "1219",
  "1116",
  "1121",
  "1413",
  "4996",
  "2765",
  "3823",
  "1115",
  "5530",
  "3860",
  "1325",
  "1317",
  "3825",
  "1149",
  "5919",
  "4933",
  "1127",
  "4971",
  "3766",
  "4672",
  "3920",
  "2360",
  "4972",
  "3460",
  "2748",
  "1434",
  "5921",
  "1318",
  "1241",
  "1415",
  "1420",
  "2646",
  "2721",
  "4950",
  "2757",
  "4669",
  "1319",
  "1516",
  "2666",
  "2625",
  "5988",
  "5008",
  "1517",
  "1518",
  "3820",
  "3795",
  "4978",
  "5942",
  "2761",
  "4675",
  "3016",
  "1015",
  "5022",
  "1026",
  "4023",
  "3019",
  "3021",
  "5017",
  "3018",
  "1014",
  "3011",
  "1013",
  "0002",
  "0001",
  "0004",
  "4024",
  "4941",
  "2655",
  "2658",
  "4864",
  "4979",
  "1421",
  "2357",
  "2622",
  "5532",
  "1422",
  "3848",
  "2641",
  "1136",
  "5851",
  "1131",
  "1122",
  "1118",
  "2723",
  "5986",
  "1120",
  "1237",
  "3850",
  "1333",
  "5922",
  "2337",
  "2633",
  "4982",
  "4945",
  "2368",
  "2620",
  "2661",
  "2626",
  "5535"
}


for code in college_codes:
    results = []
    for caste in caste_codes:
        print("Saving {} for college {}".format(caste, code))
        data = [
            ('collegecode[]', code),
            ('codecommunity', caste),
        ]

        resp = requests.post('http://tnea.a4n.in/home/college_search_code_results', headers=headers, cookies=cookies, data=data)
        content = resp.text

        doc = bs4.BeautifulSoup(content, 'html.parser')
        rows = doc.find(id="datatables-example").find("tbody").find_all("tr")
        fields = ["an rank", "code", "name", "district", "course", "cut off", "caste"]

        for row in rows:
            res = []
            cells = row.find_all("td")
            for cell in cells:
                res.append(cell.get_text())
            res.append(caste)
            results.append(dict(zip(fields, res)))

    with open(code + ".json", 'w') as f:
        f.write(json.dumps(results))
