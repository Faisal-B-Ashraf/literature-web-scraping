# Research Paper Search Web Sraping

This tool allows you to search for research papers using **Google Scholar** and **PubMed**. It leverages the `scholarly` library for Google Scholar and the `Bio.Entrez` module for PubMed, making it a useful for retrieving academic papers and their metadata.

## Features

- Search for papers on Google Scholar and retrieve:
  - Title
  - Authors
  - Number of citations
- Search for papers on PubMed and retrieve:
  - PubMed ID
  - Full MEDLINE record

## Requirements

To run this script, you need to install the following Python libraries:
- `scholarly`: For accessing Google Scholar
- `pandas`: For data manipulation (optional, not heavily used here)
- `biopython`: For accessing PubMed through the Entrez module

### Install dependencies

You can install the required libraries using pip:

```bash
pip install scholarly pandas biopython
```

## How to Use

### 1. Google Scholar Search

This function retrieves research paper metadata from Google Scholar:

```python
search_papers(query, num_results=10)
```

- `query`: The search term (e.g., `"Reservoir GHG emissions"`)
- `num_results`: The number of papers to retrieve (default is 10)

#### Example Output

For the query `"Reservoir GHG emissions"`, the script prints:

```
1. Title: Title of Paper 1
   Authors: Author1, Author2
   Citations: 45
----------------------------
2. Title: Title of Paper 2
   Authors: AuthorA, AuthorB
   Citations: 120
----------------------------
```

### 2. PubMed Search

This function retrieves research paper metadata from PubMed:

```python
search_pubmed(query, num_results=10, email="your-email@example.com")
```

- `query`: The search term (e.g., `"Reservoir GHG emissions"`)
- `num_results`: The number of papers to retrieve (default is 10)
- `email`: Your email address for Entrez API usage (replace `"your-email@example.com"` with your actual email)

#### Example Output

For the query `"Reservoir GHG emissions"`, the script prints:

```
1. PubMed ID: 12345678
   Record: Full MEDLINE record for paper 1
----------------------------
2. PubMed ID: 87654321
   Record: Full MEDLINE record for paper 2
----------------------------
```

### Running the Script

To run the script, use the following command:

```bash
python script_name.py
```

Replace `script_name.py` with the name of your script file.

### Example Workflow

1. Update the `query` variable with your search term.
2. Set the desired `num_results` for the number of papers to retrieve.
3. Provide your valid email address for PubMed API usage.

Run the script to retrieve and display the search results.

## Limitations

- **Google Scholar**: The `scholarly` library may have limitations or restrictions due to Google Scholar's anti-scraping policies.
- **PubMed**: Ensure you provide a valid email address to comply with NCBI's API usage policies.

## Contributing

If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
