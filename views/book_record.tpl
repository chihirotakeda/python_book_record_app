<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Book record</title>
</head>
<body>
    <h1>Book List</h1>
    <button type="button" name="add_book" value="add" onclick="location.href='/add_book'">New Book</button>
    <table border=1>
        <tr>
            <th>Title</th>
            <th>Volume</th>
            <th>Author</th>
            <th>Publisher</th>
            <th>Memo</th>
            <th>Action</th>
        </tr>
       %for book in books:
        <tr>
            <td>{{book["title"]}}</td>
            <td>{{book["volume"]}}</td>
            <td>{{book["author"]}}</td>
            <td>{{book["publisher"]}}</td>
            <td>{{book["memo"]}}</td>
            <td><a href="/book_del/{{book["title"]}}">remove</a></td>
        <tr>
        %end
    </table>
</body>