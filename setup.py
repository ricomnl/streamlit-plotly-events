import setuptools

setuptools.setup(
    name="streamlit-plotly-events-retro",
    version="0.0.8",
    author="Ellie Jones",
    author_email="ellie@altaml.com",
    description="Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit.",
    long_description="Plotly chart component for Streamlit that also allows for events to bubble back up to Streamlit.",
    long_description_content_type="text/plain",
    url="https://github.com/ricomnl/streamlit-plotly-events",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.63",
        "plotly >= 4.14.3",
    ],
)
