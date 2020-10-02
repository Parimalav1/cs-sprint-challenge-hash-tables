# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    d = {}
    for file_name in files:
        last = file_name.split('/')[-1]
        if last in d:
            d[last].append(file_name)
        else:
            d[last] = [file_name]
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
