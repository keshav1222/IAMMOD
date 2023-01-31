import requests
import os

api_user = "t1_krrish"
api_pass = "@Amdocs_RPA_Bot2022"
url = f"https://globe.service-now.com/api/now/table/sc_task"
params = {
    "sysparm_query" : "assignment_group=922e85cfdb1e0910e74daa4dd3961990^state=1",
    "sysparm_fields" : "sys_id, number, parent"
}
req = requests.get(url, auth=(api_user, api_pass), params=params)

response = req.json()

# print(response)




count = 0
try:    

#  #for i in range(len(response['result'])):

#     count += 1
    
#     sc_task = response['result'][i]['number']
#     sys_id = response['result'][i]['sys_id']
#     Parent_Sys_id = response['result'][i]['parent']['value']
   

   
#     urlCategory = f"https://globe.service-now.com/api/now/table/sc_req_item?sysparm_query=sys_id%3D{Parent_Sys_id}"
    
#     param = {
   
#     "sysparm_query" : "state=1",
#     "sysparm_fields" : "sys_id, number,stage, requested_for, variables.application, variables.category, variables.sub_category, variables.is_file_uploaded_successfully"
#     }
    
#     responsive = requests.get(urlCategory, auth=(api_user, api_pass), params=param)
#     category = responsive.json()['result'][0]['variables.category']
#     sub_category = responsive.json()['result'][0]['variables.sub_category']
#     Application_Name_sysId = responsive.json()['result'][0]['variables.application']
#     requested_for_sysid = responsive.json()['result'][0]['requested_for']['value']

#     print(category)
#     print(sub_category)
#     print(requested_for_sysid)
#     print(Application_Name_sysId)


#     url_Get_Application_Name = f"https://globe.service-now.com/api/now/table/u_managed_application?sysparm_query=sys_id%3D{Application_Name_sysId}"
#     param = {
#      "sysparm_query" : "state=1",
#      "sysparm_fields" : "u_name"
#     }
    

#     ApplicationNameresponse = requests.get(url_Get_Application_Name, auth=(api_user, api_pass), params=param)
#     print(ApplicationNameresponse.json())

#     url_Get_Name_Requestedfor = f"https://globe.service-now.com/api/now/table/sys_user?sysparm_query=sys_id%3D{requested_for_sysid}"
#     param = {
#      "sysparm_query" : "state=1",
#      "sysparm_fields" : "name"
#     }
    

#     NameRequestedForresponse = requests.get(url_Get_Name_Requestedfor, auth=(api_user, api_pass), params=param)
#     print(NameRequestedForresponse.json())

#     url_Get_Category = f"https://globe.service-now.com/api/now/table/u_managed_access_category?sysparm_query=sys_id%3D{category}"
#     param = {
#      "sysparm_query" : "state=1",
#      "sysparm_fields" : "u_name"
#     }

#     Categoryresponse = requests.get(url_Get_Category, auth=(api_user, api_pass), params=param)
#     print(Categoryresponse.json())

#     url_Get_Sub_Category = f"https://globe.service-now.com/api/now/table/u_managed_access_configuration?sysparm_query=sys_id%3D{sub_category}"
#     param = {
#      "sysparm_query" : "state=1",
#      "sysparm_fields" : "u_name"
#     }

#     Sub_Categoryresponse = requests.get(url_Get_Sub_Category, auth=(api_user, api_pass), params=param)
#     print(Sub_Categoryresponse.json())


#     # url_Get_Requested_Name = f"https://globe.service-now.com/api/now/table/u_managed_access_configuration?sysparm_query=sys_id%3D{sub_category}"
#     # param = {
#     #  "sysparm_query" : "state=1",
#     #  "sysparm_fields" : "u_name"
#     # }

#     # Sub_Categoryresponse = requests.get(url_Get_Sub_Category, auth=(api_user, api_pass), params=param)
#     # print(Sub_Categoryresponse.json())

#     url_get_Attachment_sysid = f"https://globe.service-now.com/api/now/table/sys_attachment?sysparm_query=table_sys_id%3D{sys_id}"
#     param = {
#      "sysparm_query" : "state=1",
#      "sysparm_fields" : "sys_id"
#     }
#     attachmentssidresponse = requests.get(url_get_Attachment_sysid, auth=(api_user, api_pass), params=param)
#     attachment_sys_id = attachmentssidresponse.json()['result'][0]['sys_id']
#     # print(attachment_sys_id)
#     # print(attachmentssidresponse.json())

#     for j in range(len(url_get_download_attachment['result'])):
#         url_get_download_attachment = f"https://globe.service-now.com/api/now/attachment?sysparm_query=sys_id%3D{attachment_sys_id}"
#         param = {
#          "sysparm_query" : "state=1",
#          "sysparm_fields" : "download_link, file_name"
#         }
#         attachment_Download_response = requests.get(url_get_download_attachment, auth=(api_user, api_pass), params=param)
#         attachment_sys_id = attachmentssidresponse.json()['result'][j]['sys_id']
    
#         # print(attachment_Download_response.json())
#         downloadlink = attachment_Download_response.json()['result'][j]['download_link']
#         filename = attachment_Download_response.json()['result'][j]['file_name']
#         split_tup = os.path.splitext(filename)
#         file_extension = split_tup[1]
#         print(file_extension)
#         file_path = os.path.join("C:\\Users\\keshava\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\attachment" ,sc_task + file_extension)

#         attachment_url = downloadlink
#         r = requests.get(attachment_url, auth=(api_user, api_pass) ,allow_redirects=True)
        
#         # open(sc_task +'.xlsx', 'wb').write(r.content)
#         open(file_path, 'wb').write(r.content)


#     # url_get_download_attachment = f"https://globe.service-now.com/api/now/attachment?sysparm_query=sys_id%3D{attachment_sys_id}"
#     # param = {
#     #  "sysparm_query" : "state=1",
#     #  "sysparm_fields" : "download_link, file_name"
#     # }
#     # attachment_Download_response = requests.get(url_get_download_attachment, auth=(api_user, api_pass), params=param)
#     # attachment_sys_id = attachmentssidresponse.json()['result'][0]['sys_id']
   
#     # # print(attachment_Download_response.json())
#     # downloadlink = attachment_Download_response.json()['result'][0]['download_link']
#     # filename = attachment_Download_response.json()['result'][0]['file_name']
#     # split_tup = os.path.splitext(filename)
#     # file_extension = split_tup[1]
#     # print(file_extension)
#     # file_path = os.path.join("C:\\Users\\keshava\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\attachment" ,sc_task + file_extension)

#     # attachment_url = downloadlink
#     # r = requests.get(attachment_url, auth=(api_user, api_pass) ,allow_redirects=True)
    
#     # # open(sc_task +'.xlsx', 'wb').write(r.content)
#     # open(file_path, 'wb').write(r.content)


#     # print(request_Name_item_id)
#     print(sc_task)
#     print(Parent_Sys_id)
#     print(sys_id)
#     print(filename)
#     # print(responsive.json())
    for i in range(len(response['result'])):

        count += 1
        
        sc_task = response['result'][i]['number']
        sys_id = response['result'][i]['sys_id']
        Parent_Sys_id = response['result'][i]['parent']['value']
    

    
        urlCategory = f"https://globe.service-now.com/api/now/table/sc_req_item?sysparm_query=sys_id%3D{Parent_Sys_id}"
        
        param = {
    
        "sysparm_query" : "state=1",
        "sysparm_fields" : "sys_id, number,stage, requested_for, variables.application, variables.category, variables.sub_category, variables.is_file_uploaded_successfully"
        }
        
        responsive = requests.get(urlCategory, auth=(api_user, api_pass), params=param)
        category = responsive.json()['result'][0]['variables.category']
        sub_category = responsive.json()['result'][0]['variables.sub_category']
        Application_Name_sysId = responsive.json()['result'][0]['variables.application']
        requested_for_sysid = responsive.json()['result'][0]['requested_for']['value']

        print(category)
        print(sub_category)
        print(requested_for_sysid)
        print(Application_Name_sysId)


        url_Get_Application_Name = f"https://globe.service-now.com/api/now/table/u_managed_application?sysparm_query=sys_id%3D{Application_Name_sysId}"
        param = {
        "sysparm_query" : "state=1",
        "sysparm_fields" : "u_name"
        }
        

        ApplicationNameresponse = requests.get(url_Get_Application_Name, auth=(api_user, api_pass), params=param)
        print(ApplicationNameresponse.json())

        url_Get_Name_Requestedfor = f"https://globe.service-now.com/api/now/table/sys_user?sysparm_query=sys_id%3D{requested_for_sysid}"
        param = {
        "sysparm_query" : "state=1",
        "sysparm_fields" : "name"
        }
        

        NameRequestedForresponse = requests.get(url_Get_Name_Requestedfor, auth=(api_user, api_pass), params=param)
        print(NameRequestedForresponse.json())

        url_Get_Category = f"https://globe.service-now.com/api/now/table/u_managed_access_category?sysparm_query=sys_id%3D{category}"
        param = {
        "sysparm_query" : "state=1",
        "sysparm_fields" : "u_name"
        }

        Categoryresponse = requests.get(url_Get_Category, auth=(api_user, api_pass), params=param)
        print(Categoryresponse.json())

        url_Get_Sub_Category = f"https://globe.service-now.com/api/now/table/u_managed_access_configuration?sysparm_query=sys_id%3D{sub_category}"
        param = {
        "sysparm_query" : "state=1",
        "sysparm_fields" : "u_name"
        }

        Sub_Categoryresponse = requests.get(url_Get_Sub_Category, auth=(api_user, api_pass), params=param)
        print(Sub_Categoryresponse.json())


       


        
        url_get_Attachment_sysid = f"https://globe.service-now.com/api/now/table/sys_attachment?sysparm_query=table_sys_id%3D{sys_id}"
        
        param = {
        "sysparm_query" : "state=1",
        "sysparm_fields" : "sys_id"
        }
        count_file  = 0
        
        attachmentssidresponse = requests.get(url_get_Attachment_sysid, auth=(api_user, api_pass), params=param)
        for j in range(len(attachmentssidresponse.json()['result'])):

            attachment_sys_id = attachmentssidresponse.json()['result'][j]['sys_id']
            # print(attachment_sys_id)
            # print(attachmentssidresponse.json())


            url_get_download_attachment = f"https://globe.service-now.com/api/now/attachment?sysparm_query=sys_id%3D{attachment_sys_id}"
            param = {
            "sysparm_query" : "state=1",
            "sysparm_fields" : "download_link, file_name"
            }
            attachment_Download_response = requests.get(url_get_download_attachment, auth=(api_user, api_pass), params=param)
            attachment_sys_id = attachmentssidresponse.json()['result'][0]['sys_id']

            # print(attachment_Download_response.json())
            downloadlink = attachment_Download_response.json()['result'][0]['download_link']
            filename = attachment_Download_response.json()['result'][0]['file_name']

            split_tup = os.path.splitext(filename)

            file_name = split_tup[0]
            file_extension = split_tup[1]
            print(file_extension)

            if(file_extension == ".xlsx"):
                count_file += 1
            

        if(count_file == 1 and file_extension == ".xlsx"):
            path = os.path.join("C:\\Users\\keshava\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\attachment", sc_task)
            os.mkdir(path)
            file_path = os.path.join(path ,file_name + file_extension)
            # file_path = os.path.join("C:\\Users\\keshava\\OneDrive - AMDOCS\\Backup Folders\\Desktop\\attachment" ,file_name + file_extension)

            attachment_url = downloadlink
            r = requests.get(attachment_url, auth=(api_user, api_pass) ,allow_redirects=True)
                
            # open(sc_task +'.xlsx', 'wb').write(r.content)
            open(file_path, 'wb').write(r.content)
        elif count_file == 0:
            print("There is no Excel File attached")
        else :
            print("More Than two Excel attached ")
        print(count_file)    
        print(sc_task)
        print(Parent_Sys_id)
        print(sys_id)
        print(filename)




except IndexError:
    print("No Open tickect Found")
except :
    print("Something else Went Wrong")
print (count)
