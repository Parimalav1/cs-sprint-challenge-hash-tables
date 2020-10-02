# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    d = {}
    for file_ in files:
        last = file_.split('/')[-1]
        if last in d:
            d[last].append(file_)
        else:
            d[last] = [file_]
    for qname in queries:
        if qname in d:
            result += d[qname]

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
