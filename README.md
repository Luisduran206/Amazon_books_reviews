# Amazon Books Reviews

# Context 

Modern big enterprises are now trying to focus all efforts in order to take advantage of new technologies and all useful tools it brings. Just like Amazon.

What makes Amazon greater than other big enterprises? The short answer is efficiency and fast response to clients demands, but also Amazon occupies all available data to improve their processes and keep customer's attention. So that every sell, qualification or review represents an opportunity to be better.

# 1\. Description of the problem

Every day, Amazon has millions of sales of items or services in many areas. Products and services, as well as their quality, are very important, so it is important to take into account sales ratings.  
In this case, the document 'Books\_rating.csv' consists of a compilation of reviews made about the sale of books on Amazon. So as Amazon wants to increase their sales, giving more visibility to the products that have better reviews and opinions among customers would be an interesting strategy to enhance sales. For this dataset, book sales.

#  	2\. Need for Big Data and Cloud

In today's context, companies like Amazon handle massive amounts of data from various sources: purchases, customer reviews, service inquiries, inventories, and more. This vast amount of information is known as Big Data, and utilizing technologies that enable efficient and real-time processing and analysis is essential.

#### **Importance of Big Data**

1. **Volume**: Amazon generates millions of data points daily, and the Books\_rating.csv file is just a small sample. Managing this data requires systems capable of storing and processing large volumes without performance issues.  
2. **Velocity**: The speed at which this data is generated demands tools that can process the information almost in real-time to enable swift decision-making.  
3. **Veracity**: Maintaining data quality and detecting anomalies is crucial to ensuring analyses are accurate and actionable.  
4. **Value**: Data analysis provides key insights into trends, customer behavior patterns, and areas for improvement in products or services.

#### **The Need for Cloud Computing**

Processing and analyzing Big Data requires significant computational resources. This is where cloud computing becomes vital, offering key advantages:

* **Scalability**: Cloud systems allow resource scaling based on demand. If the volume of data increases, as it often does with Amazon reviews, cloud systems can adapt to handle the additional load seamlessly.  
* **Accessibility**: Cloud infrastructure ensures that data and tools are available anytime and anywhere.  
* **Integration with Advanced Tools**:  
  * Google Cloud enables the use of advanced analytical tools like Spark.  
* **Massive and Distributed Storage**: Cloud technologies facilitate storing large volumes of data in distributed systems, improving data availability and security


# 	3\. Data description

Our dataset (Book\_ratings.csv) was sourced from kaggle.com, a well-known platform for data science and machine learning projects. The dataset has a size of 2.7 GB, making it suitable for demonstrating the capabilities of Big Data tools. It contains detailed information about book reviews on Amazon (+500,000), organized into the following structure:

* **Id**: A unique identifier for each book.  
* **Title**: The title of the book being reviewed.  
* **Price**: The price of the book.  
* **User\_id**: A unique identifier for the user who posted the review.  
* **profileName**: The name associated with the user’s profile.  
* **review/helpfulness**: A ratio indicating how helpful other users found the review.  
* **review/score**: The numeric rating given to the book   
* **review/time**: The timestamp of when the review was posted.  
* **review/summary**: A short summary or title of the review.  
* **review/text**: The full textual content of the review.

# 	4\. Application description

#### **Application Description**

The goal is to:

* Compute aggregate metrics, such as average review scores, prices, sentiment polarity, and subjectivity.  
* Perform sentiment analysis on customer reviews to gauge overall customer satisfaction.  
* Provide insights into product quality and customer preferences to improve decision-making.

**Platform**

* **Programming Language**: Python.  
* **Framework**:  
  * **PySpark**  
  * **TextBlob**: A Python library for natural language processing, specifically for sentiment analysis.  
* **Development Environment**: Visual Studio.

**Infrastructure**

1. **Compute Resources**:  
   * **Cloud Services** : Google Cloud.  
2. **Storage**:  
   * **Cloud Storage**: Google Cloud Storage.  
   * **Link to the Bucket(Output):** [ttps://console.cloud.google.com/storage/browser/my\_project\_88523](https://console.cloud.google.com/storage/browser/my_project_88523)  
3. **Big Data Infrastructure**:  
   * **Apache Spark**: A distributed computing system for handling large-scale data processing tasks.  
   * **Cluster Management**: Dataproc (Google Cloud) 

For accessing the bucket you must have access as Viewer in the Project called “(Grupo-4)”

# 5\. Software design

The software design emphasizes efficiency and scalability for processing large datasets with distributed computing. It provides PySpark data processing capabilities that let the application handle batch-oriented transformations and aggregations on large volumes of data. The TextBlob model is designed for natural language processing or sentiment analysis to give richer insights that can be derived from a dataset.

The application has a modular design, which shows increased modularity in separating concerns like data ingestion, sentiment analysis, and result aggregation. This boosts maintainability and allows integration of new features into the application. Finally, the application is platform-independent.

It uses functional programming within PySpark to ensure that Big Data operations are performed efficiently, and it adds a shoulder for cloud storage and cloud computation in order to make the application flexible enough for both development and production-level deployment.

# 	6\. Usage

This output file summarizes aggregated book review data from the dataset. Each row contains a unique book ID  and its corresponding title, alongside calculated metrics:

1. **avg\_review\_score**: The average review score for the book, reflecting user ratings.  
2. **avg\_polarity**: The average sentiment polarity  
3. **avg\_subjectivity**: The average subjectivity score

For example, the book titled "Theatres of San Francisco" has an average review score of 68.8, a polarity of 0.1296, and a subjectivity of 0.3632, indicating slightly positive and moderately objective reviews.

We use this command to create the cluster: gcloud dataproc clusters create amazonspark \--region=europe-southwest1 \--master-machine-type=e2-standard-4 \--master-boot-disk-size=50 \--worker-machine-type=e2-standard-4 \--worker-boot-disk-size=50 \--enable-component-gateway \--public-ip-address \--properties "dataproc:pip.packages= textblob== 0.18.0.post0" 

And this one to execute the job: BUCKET=gs://my\_project\_88523

gcloud dataproc jobs submit pyspark \--cluster amazonspark \--region=us-central1 amazon\_books\_reviews.py \-- $BUCKET/Books\_rating.csv $BUCKET/Salida1

# 	7\. Performance evaluation

# 	8\. Advanced features

This script incorporates advanced features for analyzing book reviews using Apache Spark and TextBlob. The key components include:

1. **Tools/Platforms**:  
   * Apache Spark.  
   * TextBlob: A library for sentiment analysis, integrated via Spark UDFs.  
   * Google Cloud Dataproc  
2. **Advanced Functions**:  
   * Custom UDFs (get\_polarity and get\_subjectivity) for sentiment analysis.  
   * Aggregation and rounding of metrics using avg and round functions for precision.  
   * Sorting results using orderBy for better insights.  
3. **Techniques to Mitigate Overheads**:  
   * Distributed processing with Spark for handling the 2.7 GB dataset efficiently.  
   * Columnar operations and optimized Spark aggregations to reduce execution time.  
4. **Challenging Implementation Aspects**:  
   * Integrating TextBlob with Spark, which required managing external libraries and ensuring cluster-wide dependency availability.  
   * Handling null or invalid text gracefully to avoid runtime errors during UDF execution.

# 	9\. Conclusions

This project demonstrates the effectiveness of integrating Big Data and Cloud for massive data analysis. Apache Spark and Google Cloud Platform enable efficient, scalable, and reproducible complex analyses. Future extensions will include predictive analysis and real-time visualization.

# 	10\. References

 \- Kaggle: Dataset "Amazon Books Review" https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews?resource=download )  
 \- Apache Spark Documentation ([https://spark.apache.org/docs/](https://spark.apache.org/docs/))  
 \- Google Cloud Dataproc (https://cloud.google.com/dataproc/) 
