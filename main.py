from fasthtml import common as fh

hdrs = (
    fh.Link(rel="preconnect", href="https://fonts.googleapis.com"),
    fh.Link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
    fh.Link(
        href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap",
        rel="stylesheet",
    ),
)

app, rt = fh.fast_app(live=True, hdrs=hdrs)


@rt("/")
def get():
    return fh.Titled(
        "Kasper Junge",
        fh.Container(
            fh.Ul(
                fh.Li(
                    "Lead AI Engineer, ",
                    fh.A(
                        "Dinero",
                        href="https://dinero.dk",
                    ),
                ),
                fh.Li(
                    "Co-founder and Chairperson of ",
                    fh.A("Danish Data Science Community", href="https://ddsc.io"),
                ),
                fh.Li(
                    "Co-founder and Host of ",
                    fh.A("Verbos Podcast", href="https://verbospodcast.dk"),
                ),
                fh.Li(
                    "Co-founder and Lead Frontend Developer at ",
                    fh.A("aijobs.dk", href="https://aijobs.dk"),
                ),
            ),
            fh.Style(
                """
                body { 
                    font-family: 'Roboto', sans-serif;
                    line-height: 1.6; 
                    color: #333; 
                    max-width: 800px; 
                    margin: 0 auto; 
                    padding: 20px; 
                    
                }
                h1 { 
                    color: #2c3e50; 
                    font-weight: 700;
                    font-size: 2.5em;
                    margin-bottom: 30px;
                }
                ul { 
                    padding-left: 20px; 
                    list-style-type :circle;
                }


            """
            ),
        ),
    )


fh.serve()
