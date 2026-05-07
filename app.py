from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Mind Beyond Limits</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: Arial, Helvetica, sans-serif;
        }

        body{
            background: linear-gradient(135deg, #0f172a, #1e293b);
            color: white;
            overflow-x:hidden;
        }

        header{
            padding:20px 10%;
            display:flex;
            justify-content:space-between;
            align-items:center;
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            position: sticky;
            top:0;
            z-index:1000;
        }

        .logo{
            font-size:28px;
            font-weight:bold;
            color:#38bdf8;
        }

        nav a{
            color:white;
            text-decoration:none;
            margin-left:25px;
            transition:0.3s;
        }

        nav a:hover{
            color:#38bdf8;
        }

        .hero{
            min-height:90vh;
            display:flex;
            align-items:center;
            justify-content:center;
            padding:50px 10%;
            gap:60px;
            flex-wrap:wrap;
        }

        .hero-text{
            flex:1;
            min-width:300px;
        }

        .hero-text h1{
            font-size:60px;
            margin-bottom:20px;
            line-height:1.1;
        }

        .hero-text span{
            color:#38bdf8;
        }

        .hero-text p{
            font-size:18px;
            line-height:1.8;
            color:#d1d5db;
            margin-bottom:30px;
        }

        .btn{
            display:inline-block;
            padding:15px 35px;
            background:#38bdf8;
            color:#0f172a;
            text-decoration:none;
            font-weight:bold;
            border-radius:10px;
            transition:0.3s;
        }

        .btn:hover{
            transform:translateY(-3px);
            background:#0ea5e9;
        }

        .book-container{
            flex:1;
            display:flex;
            justify-content:center;
            min-width:300px;
        }

        .book{
            width:300px;
            height:450px;
            background: linear-gradient(145deg, #38bdf8, #2563eb);
            border-radius:15px;
            box-shadow:0 20px 50px rgba(0,0,0,0.5);
            padding:30px;
            position:relative;
            transform:rotate(-5deg);
            transition:0.4s;
        }

        .book:hover{
            transform:rotate(0deg) scale(1.03);
        }

        .book h2{
            font-size:36px;
            margin-top:80px;
            line-height:1.2;
        }

        .book p{
            margin-top:20px;
            font-size:18px;
        }

        .tag{
            position:absolute;
            top:20px;
            right:20px;
            background:white;
            color:#2563eb;
            padding:8px 15px;
            border-radius:30px;
            font-weight:bold;
        }

        .features{
            padding:80px 10%;
            text-align:center;
        }

        .features h2{
            font-size:40px;
            margin-bottom:50px;
        }

        .feature-grid{
            display:grid;
            grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
            gap:30px;
        }

        .card{
            background:rgba(255,255,255,0.05);
            padding:30px;
            border-radius:20px;
            transition:0.3s;
            backdrop-filter:blur(10px);
        }

        .card:hover{
            transform:translateY(-10px);
            background:rgba(255,255,255,0.08);
        }

        .card h3{
            margin-bottom:15px;
            color:#38bdf8;
        }

        .testimonial{
            padding:80px 10%;
            text-align:center;
        }

        .testimonial h2{
            margin-bottom:40px;
            font-size:40px;
        }

        .quote{
            max-width:800px;
            margin:auto;
            background:rgba(255,255,255,0.05);
            padding:40px;
            border-radius:20px;
            font-size:20px;
            line-height:1.8;
            color:#d1d5db;
        }

        .author{
            margin-top:25px;
            color:#38bdf8;
            font-weight:bold;
        }

        .cta{
            padding:100px 10%;
            text-align:center;
        }

        .cta h2{
            font-size:50px;
            margin-bottom:20px;
        }

        .cta p{
            color:#d1d5db;
            margin-bottom:40px;
            font-size:20px;
        }

        footer{
            padding:30px;
            text-align:center;
            background:rgba(255,255,255,0.05);
            color:#9ca3af;
        }

        @media(max-width:768px){

            .hero-text h1{
                font-size:42px;
            }

            .hero{
                text-align:center;
            }

            nav{
                display:none;
            }
        }
    </style>
</head>

<body>

    <header>
        <div class="logo">BookVerse</div>

        <nav>
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Reviews</a>
            <a href="#">Contact</a>
        </nav>
    </header>

    <section class="hero">

        <div class="hero-text">
            <h1>Unlock The <span>Power</span> Of Your Mind</h1>

            <p>
                Discover transformational principles, powerful mental frameworks,
                and life-changing wisdom that can help you break limitations,
                achieve success, and become unstoppable.
            </p>

            <a href="#" class="btn">Get The Book</a>
        </div>

        <div class="book-container">
            <div class="book">
                <div class="tag">BESTSELLER</div>

                <h2>The Mind Beyond Limits</h2>

                <p>
                    A transformational guide to mastering mindset,
                    discipline, purpose, and personal growth.
                </p>
            </div>
        </div>

    </section>

    <section class="features">

        <h2>Why Readers Love This Book</h2>

        <div class="feature-grid">

            <div class="card">
                <h3>Powerful Lessons</h3>
                <p>
                    Learn practical principles that can radically improve
                    your life and mindset.
                </p>
            </div>

            <div class="card">
                <h3>Easy To Read</h3>
                <p>
                    Written in a simple and engaging style for readers
                    of every level.
                </p>
            </div>

            <div class="card">
                <h3>Life Changing</h3>
                <p>
                    Gain motivation, clarity, and confidence to pursue
                    your goals fearlessly.
                </p>
            </div>

        </div>

    </section>

    <section class="testimonial">

        <h2>What Readers Are Saying</h2>

        <div class="quote">
            "This book completely changed how I think about discipline,
            growth, and success. Every chapter felt like a breakthrough."

            <div class="author">
                — Michael Johnson
            </div>
        </div>

    </section>

    <section class="cta">

        <h2>Start Your Transformation Today</h2>

        <p>
            Join thousands of readers discovering the mindset needed
            to unlock greatness.
        </p>

        <a href="#" class="btn">Order Your Copy</a>

    </section>

    <footer>
        © 2026 BookVerse. All Rights Reserved.
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
