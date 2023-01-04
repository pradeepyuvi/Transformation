from __future__ import print_function
import json

def find_values(id, json_repr):
    results = []

    def _decode_dict(a_dict):
        try:
            results.append(a_dict[id])
        except KeyError:
            pass
        return a_dict

    json.loads(json_repr, object_hook=_decode_dict) # Return value ignored.
    return results
     
# dictt = {
#     "a" : 
#         "aa",
#     "b" : {
#         "a" : "aa"
#     }
# }


json_data = '''{
    "response": {
        "@xmlns": "http://www.hp.com/go/exstream/schema/cc-actions",
        "type": "STATUS_RESPONSE",
        "attribute": [
            {
                "@name": "status_code",
                "@value": "1001"
            },
            {
                "@name": "status_detail",
                "@value": "OK"
            },
            {
                "@name": "job_definition_name",
                "value": "EE-MEDICAID-APP-CENTER-SIT5"
            },
            {
                "@name": "description",
                "@value": ""
            },
            {
                "@name": "bundling_type",
                "@value": "Normal"
            },
            {
                "@name": "priority",
                "@value": "5"
            },
            {
                "@name": "engine_name",
                "@value": "DBCS"
            },
            {
                "@name": "job_delivery_type",
                "@value": "Fire And Forget"
            },
            {
                "@name": "job_request_type",
                "@value": "ON_DEMAND"
            },
            {
                "@name": "receive_full_report",
                "@value": "false"
            },
            {
                "@name": "variables",
                "mapOfMaps": {
                    "entryMap": [
                        {
                            "@name": "DC_RequestId",
                            "map": {
                                "entry": [
                                    {
                                        "@name": "rewritable",
                                        "@value": "true"
                                    },
                                    {
                                        "@name": "name",
                                        "@value": "DC_RequestId"
                                    },
                                    {
                                        "@name": "description",
                                        "value": "Used internally for data channel request"
                                    },
                                    {
                                        "@name": "type",
                                        "@value": "String"
                                    },
                                    {
                                        "@name": "value",
                                        "@value": ""
                                    }
                                ]
                            }
                        },
                        {
                            "@name": "SERVICE_NAME",
                            "map": {
                                "entry": [
                                    {
                                        "@name": "rewritable",
                                        "@value": "false"
                                    },
                                    {
                                        "@name": "name",
                                        "@value": "SERVICE_NAME"
                                    },
                                    {
                                        "@name": "description",
                                        "@value": ""
                                    },
                                    {
                                        "@name": "type",
                                        "@value": "String"
                                    },
                                    {
                                        "@name": "value",
                                        "@value": "getDocument"
                                    }
                                ]
                            }
                        },
                        {
                            "@name": "AGENCY",
                            "map": {
                                "entry": [
                                    {
                                        "@name": "rewritable",
                                        "@value": "false"
                                    },
                                    {
                                        "@name": "name",
                                        "@value": "AGENCY"
                                    },
                                    {
                                        "@name": "description",
                                        "@value": ""
                                    },
                                    {
                                        "@name": "type",
                                        "@value": "String"
                                    },
                                    {
                                        "@name": "value",
                                        "@value": "LDH"
                                    }
                                ]
                            }
                        },
                        {
                            "@name": "ACCOUNT_ID",
                            "map": {
                                "entry": [
                                    {
                                        "@name": "rewritable",
                                        "@value": "false"
                                    },
                                    {
                                        "@name": "name",
                                        "@value": "ACCOUNT_ID"
                                    },
                                    {
                                        "@name": "description",
                                        "@value": ""
                                    },
                                    {
                                        "@name": "type",
                                        "@value": "String"
                                    },
                                    {
                                        "@name": "value",
                                        "@value": "LDH-EE"
                                    }
                                ]
                            }
                        },
                        {
                            "@name": "OUTPUTPDF",
                            "map": {
                                "entry": [
                                    {
                                        "@name": "rewritable",
                                        "@value": "false"
                                    },
                                    {
                                        "@name": "name",
                                        "@value": "OUTPUTPDF"
                                    },
                                    {
                                        "@name": "description",
                                        "@value": ""
                                    },
                                    {
                                        "@name": "type",
                                        "@value": "File"
                                    },
                                    {
                                        "@name": "value",
                                        "value": "LA_APP_CENTER.pdf"
                                    }
                                ]
                            }
                        },
                        {
                            "@name": "%triggerJob",
                            "map": {
                                "entry": [
                                    {
                                        "@name": "rewritable",
                                        "@value": "true"
                                    },
                                    {
                                        "@name": "name",
                                        "@value": "%triggerJob"
                                    },
                                    {
                                        "@name": "description",
                                        "@value": ""
                                    },
                                    {
                                        "@name": "type",
                                        "@value": "Boolean"
                                    },
                                    {
                                        "@name": "value",
                                        "@value": "false"
                                    }
                                ]
                            }
                        },
                        {
                            "@name": "DRV",
                            "map": {
                                "entry": [
                                    {
                                        "@name": "rewritable",
                                        "@value": "true"
                                    },
                                    {
                                        "@name": "name",
                                        "@value": "DRV"
                                    },
                                    {
                                        "@name": "description",
                                        "@value": "Driver File"
                                    },
                                    {
                                        "@name": "type",
                                        "@value": "File"
                                    },
                                    {
                                        "@name": "value",
                                        "value": "/apps/stage/Pubs/AppCenterEnrollmentRequestPdfXml.xml"
                                    }
                                ]
                            }
                        },
                        {
                            "@name": "CC_JobId",
                            "map": {
                                "entry": [
                                    {
                                        "@name": "rewritable",
                                        "@value": "false"
                                    },
                                    {
                                        "@name": "name",
                                        "@value": "CC_JobId"
                                    },
                                    {
                                        "@name": "description",
                                        "@value": ""
                                    },
                                    {
                                        "@name": "type",
                                        "@value": "Integer"
                                    },
                                    {
                                        "@name": "value",
                                        "@value": "${id}"
                                    }
                                ]
                            }
                        }
                    ]
                }
            },
            {
                "@name": "starttime",
                "mapOfActionResponses": {
                    "entryMap": {
                        "@name": "starttime",
                        "action": {
                            "type": "STATUS_RESPONSE",
                            "attribute": [
                                {
                                    "@name": "status_code",
                                    "@value": "1001"
                                },
                                {
                                    "@name": "status_detail",
                                    "@value": "OK"
                                },
                                {
                                    "@name": "type",
                                    "@value": "External Program"
                                },
                                {
                                    "@name": "external_programs",
                                    "mapOfMaps": {
                                        "entryMap": {
                                            "@name": "ExternalProgram1",
                                            "map": {
                                                "entry": [
                                                    {
                                                        "@name": "extProgramReturnCode",
                                                        "@value": ""
                                                    },
                                                    {
                                                        "@name": "extProgramError",
                                                        "@value": ""
                                                    },
                                                    {
                                                        "@name": "extProgramOutPut",
                                                        "@value": ""
                                                    },
                                                    {
                                                        "@name": "update_file",
                                                        "@value": ""
                                                    },
                                                    {
                                                        "@name": "arguments",
                                                        "@value": ""
                                                    },
                                                    {
                                                        "@name": "command",
                                                        "value": "/apps/externalprogram/common/starttime.sh"
                                                    },
                                                    {
                                                        "@name": "external_program_order",
                                                        "@value": "2"
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                },
                                {
                                    "@name": "conditions",
                                    "mapOfMaps": null
                                }
                            ]
                        }
                    }
                }
            },
            {
                "@name": "First Composition",
                "mapOfActionResponses": {
                    "entryMap": {
                        "@name": "First Composition",
                        "action": {
                            "type": "STATUS_RESPONSE",
                            "attribute": [
                                {
                                    "@name": "status_code",
                                    "@value": "1001"
                                },
                                {
                                    "@name": "status_detail",
                                    "@value": "OK"
                                },
                                {
                                    "@name": "type",
                                    "value": "First Composition"
                                },
                                {
                                    "@name": "primary_package",
                                    "value": "AppCenterEnrollmentRequest_SIT5.pub"
                                },
                                {
                                    "@name": "archive_packages",
                                    "@value": "false"
                                },
                                {
                                    "@name": "varsets",
                                    "list": null
                                },
                                {
                                    "@name": "highest_engine_return_code",
                                    "@value": "Errors"
                                },
                                {
                                    "@name": "fileMappings",
                                    "mapOfMaps": {
                                        "entryMap": [
                                            {
                                                "@name": "DRV",
                                                "map": {
                                                    "entry": [
                                                        {
                                                            "@name": "dialogue_type",
                                                            "@value": "DRIVER"
                                                        },
                                                        {
                                                            "@name": "variable_name",
                                                            "@value": "DRV"
                                                        },
                                                        {
                                                            "@name": "symbolic_file",
                                                            "@value": "DRV"
                                                        }
                                                    ]
                                                }
                                            },
                                            {
                                                "@name": "OUTPUTPDF",
                                                "map": {
                                                    "entry": [
                                                        {
                                                            "@name": "dialogue_type",
                                                            "@value": "OUTPUT"
                                                        },
                                                        {
                                                            "@name": "variable_name",
                                                            "@value": "OUTPUTPDF"
                                                        },
                                                        {
                                                            "@name": "symbolic_file",
                                                            "@value": "OUTPUTPDF"
                                                        }
                                                    ]
                                                }
                                            }
                                        ]
                                    }
                                },
                                {
                                    "@name": "output_file",
                                    "@value": ""
                                }
                            ]
                        }
                    }
                }
            },
            {
                "@name": "endtime",
                "mapOfActionResponses": {
                    "entryMap": {
                        "@name": "endtime",
                        "action": {
                            "type": "STATUS_RESPONSE",
                            "attribute": [
                                {
                                    "@name": "status_code",
                                    "@value": "1001"
                                },
                                {
                                    "@name": "status_detail",
                                    "@value": "OK"
                                },
                                {
                                    "@name": "type",
                                    "@value": "External Program"
                                },
                                {
                                    "@name": "external_programs",
                                    "mapOfMaps": {
                                        "entryMap": {
                                            "@name": "ExternalProgram1",
                                            "map": {
                                                "entry": [
                                                    {
                                                        "@name": "extProgramReturnCode",
                                                        "@value": ""
                                                    },
                                                    {
                                                        "@name": "extProgramError",
                                                        "@value": ""
                                                    },
                                                    {
                                                        "@name": "extProgramOutPut",
                                                        "@value": ""
                                                    },
                                                    {
                                                        "@name": "update_file",
                                                        "@value": ""
                                                    },
                                                    {
                                                        "@name": "arguments",
                                                        "value": "${variables.SERVICE_NAME} ${variables.AGENCY} ${variables.ACCOUNT_ID} '${now()}'"
                                                    },
                                                    {
                                                        "@name": "command",
                                                        "value": "/apps/externalprogram/common/endtime.sh"
                                                    },
                                                    {
                                                        "@name": "external_program_order",
                                                        "@value": "2"
                                                    }
                                                ]
                                            }
                                        }
                                    }
                                },
                                {
                                    "@name": "conditions",
                                    "mapOfMaps": null
                                }
                            ]
                        }
                    }
                }
            },
            {
                "@name": "cluster_job_execution_mode",
                "@value": "NORMAL"
            },
            {
                "@name": "node_affinity",
                "@value": "ALL"
            },
            {
                "@name": "node_names",
                "list": null
            }
        ]
    }
}
'''
print(find_values('entryMap', json_data))
# full_data=find_values('attribute', json_repr)

