from CubeStories import *

metdadataparameters={
    "sparqlEndPointUrl":"http://macjan.datascienceinstitute.ie:8080/sparql", #endpoint of url
    "jsonMetaDataFile":"tests/JSON_Metadata_Structure.json" #JSON file with metadata
}

cubeparameters={
    "cube":"PopulationHighestEducation",  #Key value of cube
    "dimensions":["HighestEducationLevel","Gender"], #Dimensions from cube
    "measures":["Population15OrOver"], #Measures
    "hierdimensions": #Hierachical Dimension with granularity level
        {"RefArea":{ #Dimension key
            "selected_level":"CTY" # selected level
            }
        }
}

AnalysisPipeline={  ##Dictionary pair: [Pattern Key]:[List of Pattern Parameters]
    "LeagueTab":{  #League Table 

        "columns_to_order":["Population15OrOver"],
        "order_type":"asc",
        "number_of_records":5
    },
    "DissFact":{
        "dim_to_dissect":"Gender"
    }
}

a=storyTeller(metadataparameters=metdadataparameters,
                cubeparameters=cubeparameters,
                patternparameters=AnalysisPipeline)


a.tellStory()