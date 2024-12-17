# Amazon Books Reviews

---

# Context 

Modern big enterprises are now trying to focus all efforts in order to take advantage of new technologies and all useful tools it brings. Just like Amazon.

What makes Amazon greater than other big enterprises? The short answer is efficiency and fast response to clients demands, but also Amazon occupies all available data to improve their processes and keep customer's attention. So that every sell, qualification or review represents an opportunity to be better.

---

## 1\. Description of the problem

Every day, Amazon has millions of sales of items or services in many areas. Products and services, as well as their quality, are very important, so it is important to take into account sales ratings.  
In this case, the document `Books_rating.csv` consists of a compilation of reviews made about the sale of books on Amazon. So as Amazon wants to increase their sales, giving more visibility to the products that have better reviews and opinions among customers would be an interesting strategy to enhance sales. For this dataset, book sales.

##  	2\. Need for Big Data and Cloud

In today's context, companies like Amazon handle massive amounts of data from various sources: purchases, customer reviews, service inquiries, inventories, and more. This vast amount of information is known as Big Data, and utilizing technologies that enable efficient and real-time processing and analysis is essential.

#### **Importance of Big Data**

1. **Volume**: Amazon generates millions of data points daily, and the `Books_rating.csv` file is just a small sample. Managing this data requires systems capable of storing and processing large volumes without performance issues.  
2. **Velocity**: The speed at which this data is generated demands tools that can process the information almost in real-time to enable swift decision-making.  
3. **Veracity**: Maintaining data quality and detecting anomalies is crucial to ensuring analyses are accurate and actionable.  
4. **Value**: Data analysis provides key insights into trends, customer behavior patterns, and areas for improvement in products or services.

#### **The Need for Cloud Computing**

Processing and analyzing Big Data requires significant computational resources. This is where cloud computing becomes vital, offering key advantages:

* **Scalability**: Cloud systems allow resource scaling based on demand. If the volume of data increases, as it often does with Amazon reviews, cloud systems can adapt to handle the additional load seamlessly.  
* **Accessibility**: Cloud infrastructure ensures that data and tools are available anytime and anywhere.  
* **Integration with Advanced Tools**:  
  * `Google Cloud` enables the use of advanced analytical tools like `Spark`.  
* **Massive and Distributed Storage**: Cloud technologies facilitate storing large volumes of data in distributed systems, improving data availability and security


## 	3\. Data description

Our dataset `Book_ratings.csv` was sourced from `kaggle.com`, a well-known platform for data science and machine learning projects. The dataset has a size of 2.7 GB, making it suitable for demonstrating the capabilities of Big Data tools. It contains detailed information about book reviews on Amazon (+500,000), organized into the following structure:

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

Link to dataset: https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews?resource=download

## 	4\. Application description

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
   * **Link to the Bucket(Output):** [https://console.cloud.google.com/storage/browser/my\_project\_88523](https://console.cloud.google.com/storage/browser/my_project_88523)  
3. **Big Data Infrastructure**:  
   * **Apache Spark**: A distributed computing system for handling large-scale data processing tasks.  
   * **Cluster Management**: Dataproc (Google Cloud) 

For accessing the bucket you must have access as Viewer in the Project called `Grupo-4`

## 5\. Software design

The software design emphasizes efficiency and scalability for processing large datasets with distributed computing. It provides `PySpark` data processing capabilities that let the application handle batch-oriented transformations and aggregations on large volumes of data. The `TextBlob` model is designed for natural language processing or sentiment analysis to give richer insights that can be derived from a dataset.

The application has a modular design, which shows increased modularity in separating concerns like data ingestion, sentiment analysis, and result aggregation. This boosts maintainability and allows integration of new features into the application. Finally, the application is platform-independent.

It uses functional programming within `PySpark` to ensure that Big Data operations are performed efficiently, and it adds a shoulder for cloud storage and cloud computation in order to make the application flexible enough for both development and production-level deployment.

## 	6\. Usage

As mentioned above, the work was done using `Google Cloud` due to the size of the file and the number of operations performed to complete the job. To analyze the use of the application, it is recommended to review the file `amazon_books_reviews.py`.

The `textblob` library is not installed naturally in the `PySpark` environment on `Google Cloud Dataproc`. In other words, additional dependencies such as `textblob` are not automatically included in `Dataproc clusters`, so they must be installed. For best performance, it is recommended to create a new Dataproc cluster specifying the needs that are of interest, with the following command executed in the `Cloud Shell` on `Google Cloud`:
```
gcloud dataproc clusters create <name_of_cluster> \
    --region=us-central1 \
    --master-machine-type=e2-standard-2 \
    --master-boot-disk-size=50 \
    --worker-machine-type=e2-standard-2 \
    --worker-boot-disk-size=50 \
    --num-workers=2 \
    --enable-component-gateway \
    --public-ip-address \
    --properties "dataproc:pip.packages=textblob==0.18.0"
```
Attention should be paid to the `properties` argument, more specifically to `textblob==0.18.0`, where the name of the dependency you want to add is described, followed by the version of interest.

After generating the Dataproc cluster to be used, the structure of the `amazon_books_reviews.py` file must be taken into account, since the command to perform the `Spark` job must be formulated based on this. 
Therefore, it must be ensured that the input file `Books_rating.csv` is accessible and has an address in `Google Cloud`, as well as the output address, since in the application, both are input arguments to perform the work.
``` 
input_path = sys.argv[1]  # Input path
output_path = sys.argv[2]  # Output path
```
Upload `amazon_books_reviews.py` to Cloud Shell with the command:
```
gsutil cp gs://<path_to_file>/amazon_books_reviews.py .
```

Finally to run the `Spark` job, to specify the `Bucket` of interest, run in the `Cloud Shell`:
```
BUCKET=gs://<your_bucket>
```
Run the job with:
```
gcloud dataproc jobs submit <name_of_cluster> \
   --cluster amazonspark \
   --region=us-central1 amazon\_books\_reviews.py \
   -- $BUCKET/Books_rating.csv $BUCKET/Output
```
With this command, the input will be taken from the specified `Bucket` and the output will be saved in the specified bucket or address.

This output file summarizes aggregated book review data from the dataset. Each row contains a unique book ID  and its corresponding title, alongside calculated metrics:

1. **avg\_review\_score**: The average review score for the book, reflecting user ratings.  
2. **avg\_polarity**: The average sentiment polarity  
3. **avg\_subjectivity**: The average subjectivity score

For example, the book titled `"Theatres of San Francisco"` has an average review score of `68.8`, a polarity of `0.1296`, and a subjectivity of `0.3632`, indicating slightly positive and moderately objective reviews. For better understanding, you can see the file `output.csv`.

## 	7\. Performance evaluation

To test the application's performance, 3 tests of the same execution were carried out with the difference that for each one a different number of worker nodes was established. These are the machines in charge of processing and storing the data distributed in a Dataproc cluster. They execute processing and storage tasks in the cluster.
For the first test, the previous command was followed where the cluster was created, that is, the job was executed with 2 worker nodes, for said job the summary in the console was the following:
``` 
Job [87f85b11da69497ba02f9a12378c524b] finished successfully.
done: true
driverControlFilesUri: gs://dataproc-staging-us-central1-683531419655-dzspmvi6/google-cloud-dataproc-metainfo/da290109-5001-43de-a93a-3c94b5c580c4/jobs/87f85b11da69497ba02f9a12378c524b/
driverOutputResourceUri: gs://dataproc-staging-us-central1-683531419655-dzspmvi6/google-cloud-dataproc-metainfo/da290109-5001-43de-a93a-3c94b5c580c4/jobs/87f85b11da69497ba02f9a12378c524b/driveroutput
jobUuid: 763305d4-ceea-3a0c-a0c4-64ed16c2d7be
placement:
  clusterName: amazonspark
  clusterUuid: da290109-5001-43de-a93a-3c94b5c580c4
pysparkJob:
  args:
  - gs://my_project_88523/Books_rating.csv
  - gs://my_project_88523/Salida1
  mainPythonFileUri: gs://dataproc-staging-us-central1-683531419655-dzspmvi6/google-cloud-dataproc-metainfo/da290109-5001-43de-a93a-3c94b5c580c4/jobs/87f85b11da69497ba02f9a12378c524b/staging/amazon_books_reviews.py
reference:
  jobId: 87f85b11da69497ba02f9a12378c524b
  projectId: speedy-defender-436812-g6
status:
  state: DONE
  stateStartTime: '2024-12-13T12:14:15.786679Z'
statusHistory:
- state: PENDING
  stateStartTime: '2024-12-13T11:36:40.710022Z'
- state: SETUP_DONE
  stateStartTime: '2024-12-13T11:36:40.738558Z'
- details: Agent reported job success
  state: RUNNING
  stateStartTime: '2024-12-13T11:36:40.985953Z'
yarnApplications:
- name: AmazonBooksReviews
  progress: 1.0
  state: FINISHED
  trackingUrl: http://amazonspark-m.c.speedy-defender-436812-g6.internal.:8088/proxy/application_1734084873358_0003/
```
For this job, the following should be highlighted: 
Start time of job: `11:36:40.985953`
End time of job: `12:14:15.786679`
Which means a runtime of `37 minutes and 25 seconds` to complete the task using 2 worker nodes.

To increase the number of worker nodes in the cluster, this can be done by running the following command in the `Cloud Shell`:
```
gcloud dataproc clusters update <name_of_cluster> \
    --region=us-central1 \
    --num-secondary-workers=<num_of_clusters>
```

The second test was performed with 3 worker nodes, for this job the following summary was obtained:
```
Job [e3843951ccff495ba05a8b7b77feb6b6] finished successfully.
done: true
driverControlFilesUri: gs://dataproc-staging-us-central1-683531419655-dzspmvi6/google-cloud-dataproc-metainfo/da290109-5001-43de-a93a-3c94b5c580c4/jobs/e3843951ccff495ba05a8b7b77feb6b6/
driverOutputResourceUri: gs://dataproc-staging-us-central1-683531419655-dzspmvi6/google-cloud-dataproc-metainfo/da290109-5001-43de-a93a-3c94b5c580c4/jobs/e3843951ccff495ba05a8b7b77feb6b6/driveroutput
jobUuid: 2833d3ee-355a-3106-bad0-6d92f31a9272
placement:
  clusterName: amazonspark
  clusterUuid: da290109-5001-43de-a93a-3c94b5c580c4
pysparkJob:
  args:
  - gs://my_project_88523/Books_rating.csv
  - gs://my_project_88523/Salida2
  mainPythonFileUri: gs://dataproc-staging-us-central1-683531419655-dzspmvi6/google-cloud-dataproc-metainfo/da290109-5001-43de-a93a-3c94b5c580c4/jobs/e3843951ccff495ba05a8b7b77feb6b6/staging/amazon_books_reviews.py
reference:
  jobId: e3843951ccff495ba05a8b7b77feb6b6
  projectId: speedy-defender-436812-g6
status:
  state: DONE
  stateStartTime: '2024-12-13T12:52:08.505836Z'
statusHistory:
- state: PENDING
  stateStartTime: '2024-12-13T12:25:12.428641Z'
- state: SETUP_DONE
  stateStartTime: '2024-12-13T12:25:12.459637Z'
- details: Agent reported job success
  state: RUNNING
  stateStartTime: '2024-12-13T12:25:12.729501Z'
yarnApplications:
- name: AmazonBooksReviews
  progress: 1.0
  state: FINISHED
  trackingUrl: http://amazonspark-m.c.speedy-defender-436812-g6.internal.:8088/proxy/application_1734084873358_0004/
```
For this job, the following should be highlighted: 
Start time of job: `12:25:12.428641`
End time of job: `12:52:08.505836`
Which means a runtime of `26 minutes and 56 seconds` to complete the task using 3 worker nodes.

Finally, it was carried out with 4 worker nodes, for this work the following information was obtained:
```
Job [43cf0826ae7148f7a6440f9aa45022e1] finished successfully.
done: true
driverControlFilesUri: gs://dataproc-staging-us-central1-683531419655-dzspmvi6/google-cloud-dataproc-metainfo/da290109-5001-43de-a93a-3c94b5c580c4/jobs/43cf0826ae7148f7a6440f9aa45022e1/
driverOutputResourceUri: gs://dataproc-staging-us-central1-683531419655-dzspmvi6/google-cloud-dataproc-metainfo/da290109-5001-43de-a93a-3c94b5c580c4/jobs/43cf0826ae7148f7a6440f9aa45022e1/driveroutput
jobUuid: 582f227f-f896-3e0e-9bc7-904f61e1fd57
placement:
  clusterName: amazonspark
  clusterUuid: da290109-5001-43de-a93a-3c94b5c580c4
pysparkJob:
  args:
  - gs://my_project_88523/Books_rating.csv
  - gs://my_project_88523/Salida3
  mainPythonFileUri: gs://dataproc-staging-us-central1-683531419655-dzspmvi6/google-cloud-dataproc-metainfo/da290109-5001-43de-a93a-3c94b5c580c4/jobs/43cf0826ae7148f7a6440f9aa45022e1/staging/amazon_books_reviews.py
reference:
  jobId: 43cf0826ae7148f7a6440f9aa45022e1
  projectId: speedy-defender-436812-g6
status:
  state: DONE
  stateStartTime: '2024-12-13T13:19:37.167436Z'
statusHistory:
- state: PENDING
  stateStartTime: '2024-12-13T12:58:29.351564Z'
- state: SETUP_DONE
  stateStartTime: '2024-12-13T12:58:29.378367Z'
- details: Agent reported job success
  state: RUNNING
  stateStartTime: '2024-12-13T12:58:29.612698Z'
yarnApplications:
- name: AmazonBooksReviews
  progress: 1.0
  state: FINISHED
  trackingUrl: http://amazonspark-m.c.speedy-defender-436812-g6.internal.:8088/proxy/application_1734084873358_0005/
```
For last job, the following should be menctioned: 
Start time of job: `12:58:29.351564`
End time of job: `13:19:37.167436`
Which means a runtime of `20 minutes and 52 seconds` to complete the task using 4 worker nodes.

**Analysis:**
As seen in the results, by increasing the number of worker nodes, the `Spark` job execution time decreases significantly.
| Worker nodes       | Execution Time         |
|--------------------|------------------------|
| 2                  | 37 minutes 25 seconds |
| 3                  | 26 minutes 56 seconds |
| 4                  | 20 minutes 52 seconds |

This behavior highlights how distributed processing in `Spark` benefits from the increase in available computing resources, achieving greater efficiency and reduced execution times as the number of worker nodes in the cluster increases.

## 	8\. Advanced features

This script incorporates advanced features for analyzing book reviews using `Apache Spark` and `TextBlob`. The key components include:

1. **Tools/Platforms**:  
   * `Apache Spark`.  
   * `TextBlob`: A library for sentiment analysis, integrated via `Spark UDFs`.  
   * `Google Cloud Dataproc`  
2. **Advanced Functions**:  
   * Custom `UDFs (get_polarity and get_subjectivity)` for sentiment analysis.  
   * Aggregation and rounding of metrics using `avg` and `round` functions for precision.  
   * Sorting results using `orderBy` for better insights.  
3. **Techniques to Mitigate Overheads**:  
   * Distributed processing with `Spark` for handling the `2.7 GB` dataset efficiently.  
   * Columnar operations and optimized `Spark` aggregations to reduce execution time.  
4. **Challenging Implementation Aspects**:  
   * Integrating `TextBlob` with `Spark`, which required managing external libraries and ensuring cluster-wide dependency availability.  
   * Handling null or invalid text gracefully to avoid runtime errors during UDF execution.

---

# 	9\. Conclusions

This project demonstrates the effectiveness of integrating `Big Data` and `Cloud` for massive data analysis. `Apache Spark` and `Google Cloud Platform` enable efficient, scalable, and reproducible complex analyses. Future extensions could include predictive analysis, real-time visualization and more valuable insights.
This work can still be improved considerably, for example, a cleanup can be implemented in the text strings that correspond to the titles of the books followed by another series of filters that allow the elimination of different types of characters, blank spaces or capital letters that cause the same book to be separated into different records because the name was written in a different way.
A lot was learned from this project, it was a real-life use case and helped us understand the possibilities that the `Cloud` puts at our disposal.

---

# 	10\. References

 \- Kaggle: Dataset "Amazon Books Review" https://www.kaggle.com/datasets/mohamedbakhet/amazon-books-reviews?resource=download )  
 \- Apache Spark Documentation ([https://spark.apache.org/docs/](https://spark.apache.org/docs/))  
 \- Google Cloud Dataproc (https://cloud.google.com/dataproc/) 
