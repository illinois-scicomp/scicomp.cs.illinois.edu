<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>
      <%block name="title">
      SciComp Template
      </%block>
    </title>

    <!-- Bootstrap -->
    <link href="bootstrap-3.1.1-dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="css/scicomp.css" rel="stylesheet">
    <link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
    <%block name="extra_header">
    </%block>

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
      <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    <div class="navbar-wrapper">
      <div class="container">

        <div class="navbar navbar-inverse navbar-static-top" role="navigation">
          <div class="container">
            <div class="navbar-header">
              <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
              </button>
              <a class="navbar-brand" href="index.html">Scientific Computing at Illinois</a>
            </div>
            <div class="navbar-collapse collapse">
              <ul class="nav navbar-nav">
                <li><a href="people.html">People</a></li>
                <li><a href="courses.html">Courses</a></li>
                <li><a href="study.html">PhD program</a></li>
                <li class="dropdown">
                  <a href="#" class="dropdown-toggle" data-toggle="dropdown">More<b class="caret"></b></a>
                  <ul class="dropdown-menu">
                    <li><a href="news-archive.html">News Archive</a></li>
                    <li><a href="contact.html">Contact</a></li>
                  </ul>
                </li>
              </ul>
            </div>
          </div>
        </div>

      </div>
    </div>

    <%block name="full_content">
      <div class="container nonfrontpage">
        <%block name="content">
        Hi there.
        </%block>
      </div>
    </%block>

    <footer>
      <div class="container">
      <p class="pull-right"><a href="#">Back to top</a></p>
      <p><i>Have a change or suggestion?</i> Using a bitbucket account you can edit
      %for i, (descr, source_file) in enumerate(SOURCES):
        the
        <a href="https://bitbucket.org/illinois-scicomp/web/src/master/${source_file}">
          <i class="fa fa-pencil-square-o"></i>
          ${descr} (${source_file})</a>
        %if len(SOURCES) == 2 and i+1 == len(SOURCES)-1:
           or 
        %elif i+1 == len(SOURCES)-1:
          , or 
        %elif i+1 < len(SOURCES):
          ,
        %endif
      %endfor
      </p>
      <p>&copy; University of Illinois at Urbana-Champaign</p>
      </div>
    </footer>

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="js/jquery-1.11.1.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="bootstrap-3.1.1-dist/js/bootstrap.min.js"></script>
    <script src="js/holder.js"></script>
    <%block name="extra_scripts">
    </%block>
  </body>
</html>
