import requests


def get_can_summary():
    """
    Get summary on api.covid19tracker.ca and returns
    total cases and total fatalities in Canada (int x, int y)
    :return:
    """
    summary_ca = requests.get('https://api.covid19tracker.ca/summary')
    j_summary_ca = summary_ca.json()
    totalcases_ca = j_summary_ca['data'][0]['total_cases']
    totalfatalities_ca = j_summary_ca['data'][0]['total_fatalities']
    return totalcases_ca, totalfatalities_ca


def get_bc_summary():
    """
    Get all provinces summary of api.covid19tracker.ca and returns
    total cases and total fatalities in BritishColumbia. (int x and int y)
    :return:
    """
    tc_bc = 0
    tf_bc = 0
    summary_split = requests.get('https://api.covid19tracker.ca/summary/split')
    j_summary_split = summary_split.json()
    provinces = []
    province_count = 0
    len_province = len(j_summary_split['data'])
    for i in j_summary_split['data'][0]:
        if province_count <= len_province-1:
            provinces.append(j_summary_split['data'][province_count]['province'])
            province_count += 1
            if j_summary_split['data'][province_count]['province'] == 'BC':
                tc_bc = j_summary_split['data'][province_count]['total_cases']
                tf_bc = j_summary_split['data'][province_count]['total_fatalities']
            else:
                province_count += 1
                continue
        else:
            break
    return tc_bc, tf_bc


def get_yvr_summary():
    """
    Get healthregions IDs, get cases and fatalities by region IDs
    and sum them if they are from Vancouver or nearby city.
    :return:
    """
    tc_yvr = 0
    tf_yvr = 0
    healthregions = requests.get('https://api.covid19tracker.ca/province/BC/regions')
    j_healthregions = healthregions.json()
    summary_split_hr = requests.get('https://api.covid19tracker.ca/summary/split/hr')
    j_summary_split_hr = summary_split_hr.json()
    hr_bc = {}

    hr_count = 0
    for i in j_healthregions:
        if j_healthregions[hr_count]['hr_uid'] not in hr_bc:
            hr_bc[j_healthregions[hr_count]['frename']] = j_healthregions[hr_count]['hr_uid']
            hr_count += 1

    get_hr = []

    for i in hr_bc:
        if i.startswith('Vancouver') or i.startswith('Fraser'):
            get_hr.append(hr_bc[i])

    hr_count = 0
    len_hr = len(j_summary_split_hr['data'])

    for i in j_summary_split_hr['data']:
        if hr_count <= len_hr-1:
            if j_summary_split_hr['data'][hr_count]['hr_uid'] in get_hr:
                tc_yvr += j_summary_split_hr['data'][hr_count]['total_cases']
                tf_yvr += j_summary_split_hr['data'][hr_count]['total_fatalities']
                hr_count += 1
            else:
                hr_count += 1
                continue
    return tc_yvr, tf_yvr


def print_summary():
    tc1, tf1 = get_can_summary()
    tc2, tf2 = get_bc_summary()
    tc3, tf3 = get_yvr_summary()

    print("\nCONFIRMED CASES")
    print("in Canada: {}".format(tc1))
    print("in BC: {}".format(tc2))
    print("in Vancouver metropolitan area: {}".format(tc3))
    print("\nFATALITIES")
    print("in Canada: {}".format(tf1))
    print("in BC: {}".format(tf2))
    print("in Vancouver metropolitan area: {}".format(tf3))


def print_cases():
    tc1, tf1 = get_can_summary()
    tc2, tf2 = get_bc_summary()
    tc3, tf3 = get_yvr_summary()

    print("\nCONFIRMED CASES")
    print("in Canada: {}".format(tc1))
    print("in BC: {}".format(tc2))
    print("in Vancouver metropolitan area: {}".format(tc3))


def print_fatalities():
    tc1, tf1 = get_can_summary()
    tc2, tf2 = get_bc_summary()
    tc3, tf3 = get_yvr_summary()

    print("\nFATALITIES")
    print("in Canada: {}".format(tf1))
    print("in BC: {}".format(tf2))
    print("in Vancouver metropolitan area: {}".format(tf3))
