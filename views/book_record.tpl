<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Book record</title>
    <link href="../static/css/common.css" rel="stylesheet" media="all">
    <link href="https://fonts.googleapis.com/css?family=Oswald&display=swap" rel="stylesheet">
</head>
<body>
<div id="page" class="hfeed site">
<header>
    <div class="site-branding">
    <h1 class="site-title">Book List</h1>
    </div>
<nav class="nav1" role="navigation">
<ul>
    <li><a href="">Home</a></li>
    <li><a href="/book_list">Book List</a></li>
    <li><a href="/blog">Blog</a></li>
</ul>
</nav>
</header>
<main id="contents">
    <button class="newbookBtn" type="button" name="add_book" value="add" onclick="location.href='/add_book'">New Book</button>
    <table class="bookTable">
        <tr>
            <th>Book</th>
            <th>Title</th>
            <th>Author</th>
            <th>ISBN</th>
            <th>Action</th>
        </tr>
       %for book in books:
        <tr>
            <td><img src="{{book["img"]}}" alt="book{{["title"]}}"></td>
            <td>{{book["title"]}}</td>
            <td>{{book["author"]}}</td>
            <td>{{book["isbn"]}}</td>
            <td><a href="/book_del/{{book["title"]}}">remove</a></td>
        <tr>
        %end
    </table>
    </main>
    </div>
</body>