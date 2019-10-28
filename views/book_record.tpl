<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Book record</title>
    <link href="../static/css/common.css" rel="stylesheet" media="all">
</head>
<body>
<header>
    <h1>Book List</h1>
</header>
<nav>
<ul class="nav1">
    <li><a href="">Home</a></li>
    <li><a href="/book_list">Book List</a></li>
    <li><a href="">item3</a></li>
</ul>
</nav>
<main id="contents">
    <button class="newbookBtn" type="button" name="add_book" value="add" onclick="location.href='/add_book'">New Book</button>
    <table class="bookTable">
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
    </main>
</body>