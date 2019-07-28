from CubeStories import storyTeller

metdadataparameters={
    "sparqlEndPointUrl":"http://macjan.datascienceinstitute.ie:8080/sparql", #endpoint of url
    "jsonMetaDataFile":"tests/JSON_Metadata_Structure.json" #JSON file with metadata
}

cubeparameters={
    "cube":"ChildrenBySizeFamily",  #Key value of cube
    "dimensions":["FamilySize"], #Dimensions from cube
    "measures":["Children"], #Measures
    "hierdimensions": #Hierachical Dimension with granularity level
        {"RefArea":{ #Dimension key
            "selected_level":"CTY" # selected level
            }
        }
}

#cubeparameters=dict()

AnalysisPipeline={  ##Dictionary pair: [Pattern Key]:[List of Pattern Parameters]
    
    "LeagueTab":{   
       "columns_to_order":["FamilySize"],
       "order_type":"desc",
       "number_of_records":20
   },
   "DissFact":{
        "dim_to_dissect":"RefArea"
    },
   "MeasCount":{
       "count_type":"min"
   }


}

a=storyTeller(metadataparameters=metdadataparameters,
                cubeparameters=cubeparameters,
                patternparameters=AnalysisPipeline)


a.tellStory()

x=(a.showStory())

print(x["LeagueTab"])