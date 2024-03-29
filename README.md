# CubeStories
CubeStories allows querying Linked Open Statistical by Providing parameters in a form of Python dictionaries(JSON).

Reserach paper underpinning the implementation [Research paper](https://www.researchgate.net/publication/333227519_Mediating_Open_Data_Consumption_-_Identifying_Story_Patterns_for_Linked_Open_Statistical_Data)

High-level encapsulation of datastories librabry [DataStories repo](https://github.com/MaciejJanowski/DataStoryPatternLibrary)

Test sripts are available at: [Test repor](https://github.com/MaciejJanowski/CubeStoriesTesting)

### Installation
```python
pip install cubestories
```
Requirements will be automatically installed with package

### Import/Usage 
```python
from CubeStories import *

```
# Usage 
Library implements 3 artifacts required for Data analysis

* Metadata Parameters - metadata required for SPARQL queries
```json
    {
    "sparqlEndPointUrl":"[SPARQL ENDPOINT URL]", 
    "jsonMetaDataFile":"[directory of JSON file with metadata]" 
}
```

* Cube Parameters - what properties of cube to be retrieved from endpoint(based on JSON file provided in Metadata Parameters).
Values highlighted as: ```--- --- `` has to be specified by a user - replaced to value only
```json  
    {
    "cube":"---Key of Cube ---",  
    "dimensions":["---List of dimensions---"], 
    "measures":["---List of Measures---"], 
    "hierdimensions": 
        {"---DimKey---":{ 
            "selected_level":"---levelkey---" 
            }
        }
```

* Analysis Pipeline - JSON-based list of pattern analysis to be performed. Each Pattern will have such template provided
```json
{ 
    "---PatternName---": {  

        "parameter1":["---list of values---"],
        "parameter2":"---value---"
    },
    
    "---PatternName----":{
        "parameter1":"---pattern1 value---",
        "parameter2":["---list of values---"]
    }
}

```


# JSON Template - one of the metadata parameters
```json
{
    "---cube_key---" : {
		"title":"---title of cube---",
		"dataset_structure":"---URI for cube structure---",
        "dimensions":{
            "---dimension_key---":{
                "dimension_title":"---Title of diemnsion---",
                "dimension_url":"---URI for dimension---",
                "dimension_prefix":"---URI for dimension's values---"
            },
            "---dimension_key---":{
                "dimension_title":"---Title of diemnsion---",
                "dimension_url":"---URI for dimension---",
                "dimension_prefix":"---URI for dimension's values---"
            }
		},
		"hierarchical_dimensions":{
			"---dimension_key---":{
                "dimension_title":"---Title of diemnsion---",
                "dimension_url":"---URI for dimension---",
                "dimension_prefix":"---URI for dimension's values---",
				"dimension_levels":
				{
					"---level_key---":{
              "description":"---description of granularity level---",
              "granularity":"---integer level of granularity---"
          },
					"---level_key---":{
              "description":"---description of granularity level---",
              "granularity":"---integer level of granularity---"
          }

				}
			}
		},
		"measures":{
			"---measure_key---":{
			"measure_title":"---Title of measure---",
			"measure_url":"---URI for measure---"
			}

		}
    }
}
```
 

# Patterns Description
## Comments after ## are just for descriptive purposes. REMOVE THEM WHEN SPECIFYING PIPELINE
<!--ts-->
   * [Measurement and Counting](#MCounting)
   * [League Table](#LTable)
   * [Internal Comprison](#InternalComparison)
   * [Profile Outliers](#ProfileOutliers)
   * [Dissect Factors](#DissectFactors)
   * [Highlight Contrast](#HighlightContrast)
   * [Start Big Drill Down](#StartBigDrillDown)
   * [Start Small Zoom Out](#StartSmallZoomOut)
   * [Analysis By Category](#AnalysisByCategory)
   * [Explore Intersection](#ExploreIntersection)
   * [Narrating Change Over Time](#NarratingChangeOverTime)
   * [ExploreIntersection](#ExploreIntersection)
<!--te-->
# MCounting

  Measurement and Counting
  Arithemtical operators applied to whole dataset - basic information regarding data
    
### Attributes
 ```json
 "MeasCount":{
     "count_type":"count value"
 }

 ```
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | count_type	       |	```String```         | Type of Count to perform
 
### Output
Based on count_type value

|Count_type                |  Description   |	
  | ------------------------ | -------------|
  | raw| data without any analysis performed|
  | sum| sum across all numeric columns|
  | mean| mean across all numeric columns|
  | min| minimum values from all numeric columns|
  | max| maximum values from all numeric columns|
  | count| amount of records|


# LTable

  LeagueTable - sorting and extraction specific amount of records
    
### Attributes
 ```json
 "LeagueTab":{  
        "columns_to_order":["list of columns to order by"],
        "order_type":"type of order by",
        "number_of_records":5
    }
 ```
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | columns_to_order	       |	```list[String]```         | Set of columns to order by
  | order_type	       |	```String```         | Type of order (asc/desc)
  | number_of_records	       |	```Integer```         | Amount of records to retrieve
 
### Output
Based on sort_type value

|Sort_type                |  Description   |	
  | ------------------------ | -------------|
  | asc|ascending order based on columns provided in ```columns_to_order```|
  | desc|descending order based on columns provided in ```columns_to_order```|


# InternalComparison

  InternalComparison - comparison of numeric values related to textual values within one column
    
### Attributes
```json
 "IntComp":{
     "dims_to_compare":"dimension to compare",
     "meas_to_compare":"measure to compare",
     "comp_type":"comparison type"
 }

 ```
 
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | dims_to_compare	       |	```String```         | Dimensions, which common part will be investigated
  | meas_to_compare	       |	```String```         | Measure, which numeric values related to ```dim_to_compare``` will be processed
  | comp_type	       |	```String```         | Type of comparison to perform
 
### Output 
Independent from ```comp_type``` selected, output data will have additional column with numerical column ```meas_to_compare``` processed in specific way.

Available types of comparison ```comp_type```

|Comp_type                |  Description   |	
  | ------------------------ | -------------|
  | diffmax|difference with max value related to specific textual values from ```dims_to_compare```|
  | diffmean|difference with arithmetic mean related to specific textual values from ```dims_to_compare```|
  | diffmin|difference with minimum value related to specific textual values from ```dims_to_compare```|




# ExploreIntersection

 InternalComparison - comparison of numeric values related to textual values within one column
    
### Attributes
```json
 "IntComp":{
     "dim_to_compare":"dimension to compare",
     "meas_to_compare":"measure to compare",
     "comp_type":"comparison type"
 }

 ```
 
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | dim_to_compare	       |	```String```         | Dimension, which values will be investigated
  | meas_to_compare	       |	```String```         | Measure, which numeric values related to ```dim_to_compare``` will be processed
  | comp_type	       |	```String```         | Type of comparison to perform
 
### Output 
Independent from ```comp_type``` selected, output data will have additional column with numerical column ```meas_to_compare``` processed in specific way.

Available types of comparison ```comp_type```

|Comp_type                |  Description   |	
  | ------------------------ | -------------|
  | diffmax|difference with max value related to specific textual value|
  | diffmean|difference with arithmetic mean related to specific textual values|
  | diffmin|difference with minimum value related to specific textual value|


# ProfileOutliers

  ProfileOutliers - detection of unusual values within data (anomalies)
    
### Attributes
```json
    "ProfOut":{
        "display_type":"Gender"
    }
```
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | display_type       |	```String```         | What information display are bound to display (with/without anomalies)

### Output 
Pattern analysis using ```python scipy``` library will perform quick exploration in serach of unusual values within data.

Based on ```display_type``` parameter data will be displayed with/without ddetected unusual values.

Available types of displaying ```display_type```

|display_type                |  Description   |	
  | ------------------------ | -------------|
  | outliers_only|returns rows from dataset where unusual values were detected |
  | without_outliers|returns dataset with excluded rows where unusual values were detected |


# DissectFactors

  DissectFactors - decomposition of data based on values in dim_to_dissect
    
### Attributes
```json
    "DissFact":{
        "dim_to_dissect":"dimension to dissect"
    }
```
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | dim_to_dissect	       |	```String```         | Based on which dimension data should be decomposed

### Output 
As an output, data will be decomposed in a form of a dictionary, where each subset have values only related to specific value.
Dictionary of subdataset will be constructed as a series of paiers where key per each susbet will values from ```dim_to_dissect```
and this key value will be data, where yhis key value was occurring.

# HighlightContrast

  HighlightContrast - partial difference within values related to one textual column
    
### Attributes
```json
"HighCont":{
    "dim_to_contrast":"dimension to contrast",
    "meas_to_contrast":"measure to contrast",
    "contrast_type":"type of contrast"
}
```
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | dim_to_contrast	       |	```String```         | Textual column, from which values will be contrasted
  | meas_to_contrast	       |	```String```         | Numerical column, which values are contrasted
  | contrast_type	       |	```String```         | Type of contrast to present
 
### Output 
Independent from ```contrast_type``` selected, output data will have additional column with numerical column ```meas_to_contrast``` processed in specific way.

Available types of comparison ```contrast_type```

|Contrast_type                |  Description   |	
  | ------------------------ | -------------|
  | partofwhole| difference with max value related to specific textual value|
  | partofmax| difference with arithmetic mean related to specific textual values|
  | partofmin|difference with minimum value related to specific textual value|




# StartBigDrillDown

  StartBigDrillDown - data retrieval from multiple hierachical levels.

  This pattern can be only applied to data not stored already in DataFrame
    
### Attributes

```json
"StBigDrillDown":{
    "hierdim_drill_down":{ 
        "Key of hierarchical dimension":["dimlevel1key","dimlevel2key","dimlevel3key"] 
        }
}

```
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | hierdim_drill_down	       |```  dict{hierdim:list[str]} ```        | Hierarchical dimension with list of hierarchy levels to inspect
  

### Output 
As an output, data will be retrieved in a form of a dictionary, where each dataset will be retrieved from different hierachy level. List will be provided in```hierdim_drill_down```. Hierachy levels provided by in parameter will automatically sorted in order from most general to most detailed level based on metadata provided.


# StartSmallZoomOut

  StartSmallZoomOut - data retrieval from multiple hierachical levels.

  This pattern can be only applied to data not stored already in DataFrame
    
### Attributes

```json
"StSmallZoomOut":{
    "hierdim_zoom_out":{ 
        "Key of hierarchical dimension":["dimlevel1key","dimlevel2key","dimlevel3key"] 
        }
}
 ```

  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | hierdim_zoom_out	       |```  dict{hierdim:list[str]} ```        | Hierarchical dimension with list of hierarchy levels to inspect
  

### Output 
As an output, data will be retrieved in a form of a dictionary, where each dataset will be retrieved from different hierachy level. List will be provided in```hierdim_zoom_out```. Hierachy levels provided by in parameter will automatically sorted in order from most detaile to most general level based on metadata provided.


# AnalysisByCategory

  AnalysisByCategory - ecomposition of data based on values in dim_for_category with analysis performed on each susbet
    
### Attributes
```json
"AByCategory":{
    "dim_for_category":"dimension for categorisation",
    "meas_to_analyse":"measure to perform analysis",
    "analysis_type":"type of analysis"
}

```
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | dim_for_category	       |	```String```         |  Dimension, based on which input data will be categorised
  | meas_to_analyse	       |	```String```         | Measure, which will be analysed
  | analysis_type	       |	```String```         | Type of analysis to perform
 
### Output 
As an output, data will be decomposed in a form of a dictionary, where each subset have values only related to specific value. Such subset will get analysed based on ```analysis_type``` parameter

Available types of analysis ```analysis_type```

|Analysis_type                |  Description   |	
  | ------------------------ | -------------|
  | min| Minimum per each category|
  | max| Maximum per each category|
  | mean|Arithmetical mean per each category|
  | sum|Total value from each category|


# ExploreIntersection


### Attributes
```json
"ExpInt":{
    "dim_to_explore":"dimension to explroe across cubes"
}
```
  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | dim_to_explore	       |```	String     ```   |  Dimension, which existence within enpoint is going to be investigated
 
### Output 
Pattern will return series of datasets, where each will represent occurence of ```dim_to_explore``` in one cube

# NarratingChangeOverTime

Presenting difference between 2 numerical properties of data
### Attributes
```json
"NarrChangeOT":{
    "meas_to_narrate":["list of two dimensions to present change"],
    "narr_type":"type of narration"
}
```

  Parameter                 | Type       | Description   |	
  | :------------------------ |:-------------:| :-------------|
  | meas_to_narrate	       |	```String```         |  Set of 2 measures, which change will be narrated
  | narr_type	       |	```String```         | Type of narration to perform

### Output 
Independent from ```narr_type``` selected, output data will have additional column with numerical values processed in specific way.

Available types of analysis ```narr_type```

|Narr_type                |  Description   |	
  | ------------------------ | -------------|
  | percchange| Percentage change between first nad second property|
  | diffchange| Quantitive change between first and second property|
