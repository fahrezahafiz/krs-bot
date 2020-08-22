import requests

TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9' \
        '.eyJzdWIiOiIxMTAxNTAiLCJpcGJEbiI6InVpZD1mYWhyZXphXzEyLG91PUtPTSxvdT1GTUlQQSxvdT1TMSxvdT1TdHVkZW50LG91PVBlb3BsZSxkYz1pcGIsZGM9YWMsZGM9aWQiLCJpcGJVaWQiOiJmYWhyZXphXzEyIiwiaXBiTmFtZSI6IkZBSFJFWkEgSUtIU0FOIEhBRklaIiwiaXBiRW1haWwiOiJmYWhyZXphXzEyQGFwcHMuaXBiLmFjLmlkIiwiaXBiTmltIjoiRzY0MTcwMDc3IiwiaXBiVGlwZUFrdW4iOiJTdHVkZW50IiwiaXBiT3JhbmdJRCI6IjIzMTAwMyIsImlwYk1haGFzaXN3YUlEIjoiMTEwMTUwIiwiZXhwIjoxNTk5NzIxMzczLCJpc3MiOiJodHRwczovL2FwaS5pcGIuYWMuaWQifQ.cWC3S_snJJElOiopxBeQkCfDaSFZ90mfab3wd63htQsFEQ0phKqNNuNWhuclY6Epl_0do9jOcJbtARd1OtbHcPRlAkPJVFuwP-5uYs5-tcyPGteO0JSgvARnSssyz0GRmq_VP-4giFdpNmlLQ_75PA0xsVyUBXsaM_mUZXSgCMz8tt0UecdllDcD51S3gqvZv6sue5tRlHkV4c9BMo4DeDputbxaNS9VSXJFio3xby8cY_j2GpHo6qdRJeaBJ2xEyvqEZbkTVV9oFbHHEddj_1z1WVUTOc_vOFGvNvfgUcMSD42LbmCZQ8SoPS9IvrzCa5_W6iYkMCFp5f_64nNcFQ '
URL = 'https://krs.ipb.ac.id/api/Krs'
INTERDEPT = 2
MAYOR = 3
SC = 5

# (course_id, kuliah, praktikum, responsi, status)
COURSES = [
    # SC
    (133719, "2", "0", "0", SC),  # manajemen syariah
    (133630, "2", "0", "0", SC),  # manajemen keuangan konsumen
    (133982, "1", "0", "0", SC),  # PTN201
    # Mayor
    # (134135, "2", "0", "2", MAYOR),  # mppl
    # (134150, "2", "0", "0", MAYOR),  # mptp
    # (134167, "3", "2", "0", INTERDEPT),  # pengbio
    # (134097, "1", "0", "0", MAYOR),  # etikom
]

if __name__ == '__main__':
    # initialization
    session = requests.Session()
    session.headers.update({
        "Accept": 'application/json',
        "Content-Type": 'application/json',
        "Authorization": f"Bearer {TOKEN}"
    })

    # check token
    # res = session.get('https://krs.ipb.ac.id/api/DataHalamanRencanaStudi')
    # print(res.status_code)

    for course in COURSES:
        course_id, kuliah, praktikum, responsi, status = course
        res = session.post(URL, json={
            "DiplomaProgramKeahlianId": 0,
            "KelasKuliah": kuliah,
            "KelasPraktikum": praktikum,
            "KelasResponsi": responsi,
            "KurikulumId": course_id,
            "PascaMatrikulasi": False,
            "PascaSitIn": False,
            "StatusMataKuliahId": status
        })

        print(res.status_code, res.text)
