from setuptools import setup, find_packages

setup(
    name="opencli",
    version="1.0.0",
    author="BlazeMC404",
    author_email="your.email@example.com",
    description="Python framework for creating custom terminals and command-line shells",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/BlazeMC404/OpenCLI",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        # Add any runtime dependencies here
    ],
    entry_points={
        "console_scripts": [
            "opencli = opencli:setup",  # Modify this as necessary based on the entry-point function
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.7",
)
