#!/usr/bin/env python3
# Python implementation to find the 
# the missing end in the HTML code

# Function to Auto complete the 
# missing tag in the html Code
def autoComplete(s):
    
    # Split the html Code in line
    linesOfCode = list(s.strip().split("\n"))
    
    # Tags which are self closed doesn't
    # needs to be closed
    selfClosedTags = ["area", "base", "br", \
            "col", "embed", "hr", "img", \
            "input", "link", "meta", "param", \
                    "source", "track", "wbr"]
    n = len(linesOfCode)

    stack = []
    
    # Loop to iterate over the
    # lines of code
    for i in range(n):
        j = 0
        
        # Current Line
        line = linesOfCode[i]
        while j < len(linesOfCode[i]):
            
            # Condition to check if the current 
            # character is a end tag in the code
            if j + 1 < len(line) and line[j] == "<"\
                            and line[j + 1] == "/":
                tag = []
                j += 2
                
                # Loop to get the tag
                while j < len(line) and\
                "a" <= line[j] <= "z":
                    tag.append(line[j])
                    j += 1
                while j < len(line) and line[j] != ">":
                    j += 1
                if stack[-1] != tag:
                    tag = stack[-1]
                    return "</" + "".join(tag) + ">"
                stack.pop()
                
            # Condition to check if the current 
            # character denotes the code is 
            # of the HTML 5
            elif j + 1 < len(line) and line[j] == "<"\
                                and line[j] == "!":
                continue
                
            # Condition to check if the current 
            # tag is a start tag of the HTML Code
            elif line[j] == "<":
                tag = []
                j += 1
                
                # Loop to get the tag of the HTML
                while j < len(line) and\
                    "a" <= line[j] <= "z":
                    tag.append(line[j])
                    j += 1
                while j < len(line) and line[j] != ">":
                    j += 1
                    
                # Condition to check if the 
                # current tag is not a self closed tag
                if "".join(tag) not in selfClosedTags:
                    stack.append(tag)
            j += 1
            
    # Condition to check if any tag 
    # is unbalanced then return that tag
    if stack:
        tag = stack.pop()
        return "</" + "".join(tag) + ">"
    return -1

# Driver Code
if __name__ == "__main__":
    s = """<!DOCTYPE html>
<html lang="en">
{% load static %}
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- title block -->
    {% if title %}
        <title>Fix Mzansi - {{ title }}</title>
    {% else %}
        <title>Fix Mzansi -  Base</title>
    {% endif %}
    <!-- end title block -->

    <!-- Custom CSS -->
    <link rel="stylesheet" type="text/css" href="{% static 'css/nav_sidebar.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/body_tag.css' %}">
    <link rel="stylesheet" type="text/css" href="{% static 'css/main_page_content.css' %}">

    <!-- Bootstrap CSS link -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
</head>
<body id="body_tag" class="container-fluid">

    <!-- Nav Bar -->
    <nav id="top_nav" class="navbar bg-body-tertiary">
        <!-- Nav Bar Elements Div -->
        <div class="container-fluid">
          
          <!-- Nav Bar Small Screen button Contolling sidebar -->
          <button class="btn d-inline-block d-md-none border" alt="Menu" title="Menu">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-list" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M2.5 12a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5m0-4a.5.5 0 0 1 .5-.5h10a.5.5 0 0 1 0 1H3a.5.5 0 0 1-.5-.5"/>
            </svg>
          </button>
          <!-- End Nav Bar Small Screen button -->

          <!-- Nav Bar Small "FixMzansi" Center Logo -->
          <a class="navbar-brand align-self-center " href="#">
            <img src="{% static 'images/FixMzansi.png' %}" alt="Logo" width="150px" height="30px" class="d-inline-block">
          </a>
          <!-- End Nav Bar Small "FixMzansi" Center Logo -->

          <!-- Nav Bar Small top right Logo -->
          <a class="navbar-brand align-self-end" href="#">
            <img src="{% static 'images/logo_trans_bg.png' %}" alt="Logo" width="48" height="48" class="d-inline-block">
          </a>
          <!-- End Nav Bar Small top right Logo -->
        </div>
        <!-- End Nav Bar Elements Div -->
    </nav>
    <!-- End Nav Bar -->

    <!-- Main Content Container Div -->
    <main id="wrapper_main_div">
      <!-- Sidebar -->
      <div id="sidebar_id" class="sidebar d-md-block border border-top-0 border-bottom-0 border-start-0 position-relative">
        
        <!-- Home Button -->
        <a href="#" class="btn mb-1">
          <div id="home_icon_div" class="text-start">
            <svg id="home_icon_svg" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-app-indicator d-inline-block" viewBox="0 0 16 16">
              <path d="M5.5 2A3.5 3.5 0 0 0 2 5.5v5A3.5 3.5 0 0 0 5.5 14h5a3.5 3.5 0 0 0 3.5-3.5V8a.5.5 0 0 1 1 0v2.5a4.5 4.5 0 0 1-4.5 4.5h-5A4.5 4.5 0 0 1 1 10.5v-5A4.5 4.5 0 0 1 5.5 1H8a.5.5 0 0 1 0 1z"/>
              <path d="M16 3a3 3 0 1 1-6 0 3 3 0 0 1 6 0"/>
            </svg>
            <p class="h5">Home</p>
          </div>
        </a>
        <!-- End Home Button -->

        <!-- Log Issue Button -->
        <a href="#" class="btn mb-1">
          <div id="Log_Issue_icon_div" class="text-start">
            <svg id="log_issue_icon_svg" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
              <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
              <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5z"/>
            </svg>
            <p class="h5">Log Issue</p>
          </div>
        </a>
        <!-- End Log Issue Button -->

        <!-- Logged Issues Button -->
        <a href="#" class="btn mb-1">
          <div id="Logged_Issues_icon_div" class="text-start">            
            <svg id="logged_issues_icon_svg" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-map" viewBox="0 0 16 16">
              <path fill-rule="evenodd" d="M15.817.113A.5.5 0 0 1 16 .5v14a.5.5 0 0 1-.402.49l-5 1a.5.5 0 0 1-.196 0L5.5 15.01l-4.902.98A.5.5 0 0 1 0 15.5v-14a.5.5 0 0 1 .402-.49l5-1a.5.5 0 0 1 .196 0L10.5.99l4.902-.98a.5.5 0 0 1 .415.103M10 1.91l-4-.8v12.98l4 .8zm1 12.98 4-.8V1.11l-4 .8zm-6-.8V1.11l-4 .8v12.98z"/>
            </svg>
            <p class="h5">Logged Issues</p>
          </div>
        </a>
        <!-- End Logged Issues Button -->

        <!-- Profile Button -->
        <a href="#" class="btn mb-1">
          <div id="Profile_icon_div" class="text-start">
            <svg id="profile_icon_svg" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-person-video3" viewBox="0 0 16 16">
              <path d="M14 9.5a2 2 0 1 1-4 0 2 2 0 0 1 4 0m-6 5.7c0 .8.8.8.8.8h6.4s.8 0 .8-.8-.8-3.2-4-3.2-4 2.4-4 3.2"/>
              <path d="M2 2a2 2 0 0 0-2 2v8a2 2 0 0 0 2 2h5.243c.122-.326.295-.668.526-1H2a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v7.81c.353.23.656.496.91.783Q16 12.312 16 12V4a2 2 0 0 0-2-2z"/>
            </svg>
            <p class="h5">Profile</p>
          </div>
        </a>
        <!-- End Profile Button -->

        <!-- About Button -->
        <a href="#" class="btn mb-1">
          <div id="About_icon_div" class="text-start">
            <svg id="about_icon_svg" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-info-square" viewBox="0 0 16 16">
              <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2z"/>
              <path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0"/>
            </svg>
            <p class="h5">About</p>
          </div>
        </a>
        <!-- End About Button -->

        <!-- Horizontal line -->
        <div class="separator">
          <hr>
        </div>
        <!-- End Horizontal line -->

        <div class="bottom_container position-absolute bottom-0 start-0 end-0 mb-3 ms-3 me-3">
          <button id="bottom_button_id" href="#" class="btn btn-primary rounded bottom_button">Sign In</button>
          <button id="bottom_button_id" href="#" class="btn btn-primary rounded bottom_button">Sign Up</button>
        </div>
      </div>
      <!-- End Sidebar -->

      <!-- Page Content Block -->
      <div id="page_content" class="ps-2 pe-2 pt-2 pb-2">
        {% block content %}
        {% endblock content %}
      </div>
      <!-- End Page Content Block -->
    </main>
    <!-- Main Content Container Div -->

    <!-- Bootstrap JS link -->
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    <!-- End Bootstrap JS link -->
    
</body>
</html>"""
    tag = autoComplete(s)
    print(tag)
