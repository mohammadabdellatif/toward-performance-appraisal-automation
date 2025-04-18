from ds_extractor.issues import IssuesDatasetExtractor

if __name__ == '__main__':
    # extract issues, one record for each issue with the summary for all processing statistics
    ds_extractor = IssuesDatasetExtractor('postgresql+psycopg2://dbuser:dbpassword@localhost:5454/supportdb1',
                                          "../temp_data")
    ds_extractor.process()

    # extract issues, one record for each assignee turn (snapshot), with processing statistics summary for each assignee
    ds_extractor = IssuesDatasetExtractor('postgresql+psycopg2://dbuser:dbpassword@localhost:5454/supportdb1',
                                          "../temp_data",
                                          issues_filename="issues_snapshot.csv",
                                          separate_snapshots=True)
    ds_extractor.process()
