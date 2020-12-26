def paginated_results(results,page,limit = 10):
    total_records = len(results)
    start = (page - 1) * limit 
    
    if start > total_records:
        return []

    return results[start: start + limit]