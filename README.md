<div style="font-family: Arial, sans-serif; line-height:1.6; padding:20px;">
<h2>Nairobi Freelance Gigs API - REG-NO: C027-01-2798/2024</h2>

<p style="font-size:18px;">
This projects demonstrates how to use the modern python framework fastapi to perform crud operations.
</p>

<h3 style="color:#333;">prerequisites</h3>
<div style="margin-left:20px;">
<p>You will need the following locally installed in your machine to be able to run and demonstrate the crud operations</p>

<ul style="list-style-type:square;">
  <li>Python3</li>
  <li>Pydantic</li>
  <li>FastApi</li>
  <li>Uvicorn</li>
  <li>Python environment</li>
  <li>Pip package manager</li>
</ul>
</div>

<p>You can use a folder structure like this to successfully run this project and demontrate the crud operation</p>

<pre style="background:#f4f4f4; padding:10px; border-radius:5px;">
FastApi(parent-folder)
  >app
  >python env
</pre>

<h3 style="color:#333;">Steps of successfully running this project</h3>

<ol>
  <li>
    Inside the parent folder create a python env using this command
    <pre style="background:#f4f4f4; padding:8px; border-radius:5px;">
python3 -m venv your_env(input a random name)
    </pre>
  </li>

  <li>
    Navigate into the python env and activate it using this command
    <pre style="background:#f4f4f4; padding:8px; border-radius:5px;">
source/scripts/bin/activate
    </pre>
  </li>

  <li>
    Inside the python env install fastapi and all its packages using this command
    <pre style="background:#f4f4f4; padding:8px; border-radius:5px;">
pip install "fastapi[all]"
    </pre>
  </li>

  <li>
    Navigate back to the parent folder and you can now run your project using this uvicorn command
    <pre style="background:#f4f4f4; padding:8px; border-radius:5px;">
uvicorn app.main:app --reload --port 8000
    </pre>
  </li>
</ol>

<p style="color:#555;">
(Note that the above commands are linux based commands - you will use other commands for other OS)
</p>

<ul>
  Features of this api
  <li>Listing all the gigs available</li>
    <li>Viewing gig details by specific id</li>
    <li>Searching gig by title or descripytion</li>
    <li>Creating new gig</li>
    <li>Updating the gigs details</li>
    <li>Deleting gigs</li>
</ul>

</div>
