
# Bug Report

## Title: Search functionality does not return results unless a suggestion is selected from autocomplete  
**ID:** BUG_UI_001  
**Reported By:** Drazen
**Date Reported:** 2025-04-08  
**Environment:**  
- **URL:** https://bookcart.azurewebsites.net/  
- **Browser:** Chrome 123.0.0.0 (64-bit)
- **OS:** Windows 10 Pro

## Description:
When typing a book title or author into the search bar and pressing "Enter", no search results are returned. The search functionality only works if the user selects a suggestion from the autocomplete dropdown. This behavior is misleading and limits the usability of the search feature.

## Expected Result:
User should be able to input a search term manually (either full or partial match of book title or author) and receive relevant search results, even without selecting from the autocomplete list.

## Actual Result:
- Typing an author name (e.g., "Penny Reid") and pressing "Enter" shows no results.

## Steps to Reproduce:
1. Navigate to https://bookcart.azurewebsites.net/
2. In the search bar, type any author name (e.g., "Penny Reid")
3. Press "Enter" or click the search icon
4. Observe that **no search results** are displayed
5. Type any book name (e.g. "Dr. Strange Beard") but now **select the "Dr. Strange Beard" suggestion from the autocomplete dropdown**
6. Observe that the search **now works and returns the book**

## Severity: Medium  
## Priority: High  
## Type: Functional Bug  
## Component: UI Search  
## Reproducibility: 100%