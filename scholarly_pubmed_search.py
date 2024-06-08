from scholarly import scholarly
import pandas as pd
from Bio import Entrez

# Function to search papers on Google Scholar
def search_papers(query, num_results=10):
    search_query = scholarly.search_pubs(query)
    papers = []
    
    for i in range(num_results):
        try:
            paper = next(search_query)
            title = paper.get('bib', {}).get('title', 'N/A')
            authors = paper.get('bib', {}).get('author', 'N/A')
            num_citations = paper.get('num_citations', 'N/A')
            
            papers.append({
                'Title': title,
                'Authors': authors,
                'Citations': num_citations
            })
        except StopIteration:
            break
        
    return papers

# Function to search papers on PubMed
def search_pubmed(query, num_results=10, email="your-email@example.com"):
    Entrez.email = email
    handle = Entrez.esearch(db="pubmed", term=query, retmax=num_results)
    record = Entrez.read(handle)
    handle.close()
    
    paper_ids = record["IdList"]
    papers = []
    
    for paper_id in paper_ids:
        handle = Entrez.efetch(db="pubmed", id=paper_id, rettype="medline", retmode="text")
        paper_record = handle.read()
        handle.close()
        
        papers.append({
            'PubMed ID': paper_id,
            'Record': paper_record
        })
        
    return papers

if __name__ == "__main__":
    # Google Scholar Search
    print("### Google Scholar Search ###")
    query = "Reservoir GHG emissions"
    num_results = 10  # Number of results you want to fetch
    
    papers = search_papers(query, num_results)
    
    for i, paper in enumerate(papers):
        print(f"{i+1}. Title: {paper['Title']}")
        print(f"   Authors: {paper['Authors']}")
        print(f"   Citations: {paper['Citations']}")
        print("----------------------------")
    
    # PubMed Search
    print("### PubMed Search ###")
    email = "your-email@example.com"  # Replace with your actual email address
    papers = search_pubmed(query, num_results, email)
    
    for i, paper in enumerate(papers):
        print(f"{i+1}. PubMed ID: {paper['PubMed ID']}")
        print(f"   Record: {paper['Record']}")
        print("----------------------------")
