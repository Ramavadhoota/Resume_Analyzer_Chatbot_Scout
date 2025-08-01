
# **Deployment Guide**

This guide provides instructions for deploying the TalentScout Hiring Assistant to various cloud platforms.

## *Prerequisites*

- Git repository with the application code
- OpenAI API key
- Cloud platform account (AWS, GCP, Heroku, etc.)

## Option 1: Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy Streamlit applications.

### Steps:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and branch
   - Set the main file path: `app.py`
   - Add your OpenAI API key in the secrets section:
     ```toml
     OPENAI_API_KEY = "your-api-key-here"
     ```
   - Click "Deploy"

3. **Access Your App**
   - Your app will be available at: `https://your-app-name.streamlit.app`

## Option 2: Heroku

### Steps:

1. **Create Heroku App**
   ```bash
   heroku create your-talent-scout-app
   ```

2. **Add Buildpacks**
   ```bash
   heroku buildpacks:add heroku/python
   ```

3. **Create Procfile**
   Create a file named `Procfile` (no extension):
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set OPENAI_API_KEY=your-api-key-here
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Add Heroku deployment files"
   git push heroku main
   ```

6. **Open App**
   ```bash
   heroku open
   ```

## Option 3: AWS (EC2)

### Steps:

1. **Launch EC2 Instance**
   - Choose Ubuntu 20.04 LTS
   - Select t2.micro (free tier) or larger
   - Configure security group to allow HTTP (port 80) and HTTPS (port 443)

2. **Connect to Instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx
   ```

4. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

5. **Set Up Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. **Create Environment File**
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

7. **Create Systemd Service**
   Create `/etc/systemd/system/talentscout.service`:
   ```ini
   [Unit]
   Description=TalentScout Hiring Assistant
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/your-repo
   Environment=PATH=/home/ubuntu/your-repo/venv/bin
   ExecStart=/home/ubuntu/your-repo/venv/bin/streamlit run app.py --server.port=8501 --server.address=0.0.0.0
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

8. **Start Service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable talentscout
   sudo systemctl start talentscout
   ```

9. **Configure Nginx**
   Create `/etc/nginx/sites-available/talentscout`:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

10. **Enable Site**
    ```bash
    sudo ln -s /etc/nginx/sites-available/talentscout /etc/nginx/sites-enabled/
    sudo nginx -t
    sudo systemctl restart nginx
    ```

## Option 4: Google Cloud Platform (GCP)

### Steps:

1. **Create GCP Project**
   - Go to [console.cloud.google.com](https://console.cloud.google.com)
   - Create a new project

2. **Enable APIs**
   ```bash
   gcloud services enable run.googleapis.com
   gcloud services enable cloudbuild.googleapis.com
   ```

3. **Create Dockerfile**
   Create a `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

4. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy talentscout \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars OPENAI_API_KEY=your-api-key-here
   ```

5. **Access Your App**
   - GCP will provide a URL for your deployed application

## Option 5: Docker Deployment

### Steps:

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build Image**
   ```bash
   docker build -t talentscout .
   ```

3. **Run Container**
   ```bash
   docker run -p 8501:8501 -e OPENAI_API_KEY=your-api-key-here talentscout
   ```

4. **Access App**
   - Open browser and go to `http://localhost:8501`

## Environment Variables

Set these environment variables in your deployment:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `STREAMLIT_SERVER_PORT`: Port for the application (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: localhost)

## Security Considerations

1. **API Key Protection**
   - Never commit API keys to version control
   - Use environment variables or secrets management
   - Rotate keys regularly

2. **HTTPS**
   - Always use HTTPS in production
   - Configure SSL certificates

3. **Access Control**
   - Implement authentication if needed
   - Use firewalls and security groups

4. **Data Privacy**
   - Ensure GDPR compliance
   - Implement data retention policies
   - Secure data transmission

## Monitoring and Logging

1. **Application Logs**
   - Monitor application logs for errors
   - Set up log aggregation

2. **Performance Monitoring**
   - Monitor response times
   - Track API usage and costs

3. **Health Checks**
   - Implement health check endpoints
   - Set up automated monitoring

## Troubleshooting

### Common Issues:

1. **Port Already in Use**
   - Change the port in configuration
   - Check for other running applications

2. **API Key Issues**
   - Verify API key is correct
   - Check API key permissions and credits

3. **Dependencies Issues**
   - Ensure all requirements are installed
   - Check Python version compatibility

4. **Memory Issues**
   - Increase memory allocation
   - Optimize application code

### **Support**:

- Check Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
- OpenAI API documentation: [platform.openai.com](https://platform.openai.com)
- Platform-specific documentation for your chosen deployment method

## **Cost Optimization**

1. **API Usage**
   - Monitor OpenAI API usage
   - Implement caching where possible
   - Use appropriate model sizes

2. **Infrastructure**
   - Choose appropriate instance sizes
   - Use auto-scaling when available
   - Monitor resource usage

3. **Bandwidth**
   - Optimize application size
   - Use CDN for static assets

---

=======
# **Deployment Guide**

This guide provides instructions for deploying the TalentScout Hiring Assistant to various cloud platforms.

## *Prerequisites*

- Git repository with the application code
- OpenAI API key
- Cloud platform account (AWS, GCP, Heroku, etc.)

## Option 1: Streamlit Cloud (Recommended)

Streamlit Cloud is the easiest way to deploy Streamlit applications.

### Steps:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository and branch
   - Set the main file path: `app.py`
   - Add your OpenAI API key in the secrets section:
     ```toml
     OPENAI_API_KEY = "your-api-key-here"
     ```
   - Click "Deploy"

3. **Access Your App**
   - Your app will be available at: `https://your-app-name.streamlit.app`

## Option 2: Heroku

### Steps:

1. **Create Heroku App**
   ```bash
   heroku create your-talent-scout-app
   ```

2. **Add Buildpacks**
   ```bash
   heroku buildpacks:add heroku/python
   ```

3. **Create Procfile**
   Create a file named `Procfile` (no extension):
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set OPENAI_API_KEY=your-api-key-here
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Add Heroku deployment files"
   git push heroku main
   ```

6. **Open App**
   ```bash
   heroku open
   ```

## Option 3: AWS (EC2)

### Steps:

1. **Launch EC2 Instance**
   - Choose Ubuntu 20.04 LTS
   - Select t2.micro (free tier) or larger
   - Configure security group to allow HTTP (port 80) and HTTPS (port 443)

2. **Connect to Instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Install Dependencies**
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv nginx
   ```

4. **Clone Repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

5. **Set Up Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

6. **Create Environment File**
   ```bash
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

7. **Create Systemd Service**
   Create `/etc/systemd/system/talentscout.service`:
   ```ini
   [Unit]
   Description=TalentScout Hiring Assistant
   After=network.target

   [Service]
   User=ubuntu
   WorkingDirectory=/home/ubuntu/your-repo
   Environment=PATH=/home/ubuntu/your-repo/venv/bin
   ExecStart=/home/ubuntu/your-repo/venv/bin/streamlit run app.py --server.port=8501 --server.address=0.0.0.0
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```

8. **Start Service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable talentscout
   sudo systemctl start talentscout
   ```

9. **Configure Nginx**
   Create `/etc/nginx/sites-available/talentscout`:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:8501;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection "upgrade";
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

10. **Enable Site**
    ```bash
    sudo ln -s /etc/nginx/sites-available/talentscout /etc/nginx/sites-enabled/
    sudo nginx -t
    sudo systemctl restart nginx
    ```

## Option 4: Google Cloud Platform (GCP)

### Steps:

1. **Create GCP Project**
   - Go to [console.cloud.google.com](https://console.cloud.google.com)
   - Create a new project

2. **Enable APIs**
   ```bash
   gcloud services enable run.googleapis.com
   gcloud services enable cloudbuild.googleapis.com
   ```

3. **Create Dockerfile**
   Create a `Dockerfile`:
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

4. **Deploy to Cloud Run**
   ```bash
   gcloud run deploy talentscout \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars OPENAI_API_KEY=your-api-key-here
   ```

5. **Access Your App**
   - GCP will provide a URL for your deployed application

## Option 5: Docker Deployment

### Steps:

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   COPY requirements.txt .
   RUN pip install -r requirements.txt

   COPY . .

   EXPOSE 8501

   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build Image**
   ```bash
   docker build -t talentscout .
   ```

3. **Run Container**
   ```bash
   docker run -p 8501:8501 -e OPENAI_API_KEY=your-api-key-here talentscout
   ```

4. **Access App**
   - Open browser and go to `http://localhost:8501`

## Environment Variables

Set these environment variables in your deployment:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `STREAMLIT_SERVER_PORT`: Port for the application (default: 8501)
- `STREAMLIT_SERVER_ADDRESS`: Server address (default: localhost)

## Security Considerations

1. **API Key Protection**
   - Never commit API keys to version control
   - Use environment variables or secrets management
   - Rotate keys regularly

2. **HTTPS**
   - Always use HTTPS in production
   - Configure SSL certificates

3. **Access Control**
   - Implement authentication if needed
   - Use firewalls and security groups

4. **Data Privacy**
   - Ensure GDPR compliance
   - Implement data retention policies
   - Secure data transmission

## Monitoring and Logging

1. **Application Logs**
   - Monitor application logs for errors
   - Set up log aggregation

2. **Performance Monitoring**
   - Monitor response times
   - Track API usage and costs

3. **Health Checks**
   - Implement health check endpoints
   - Set up automated monitoring

## Troubleshooting

### Common Issues:

1. **Port Already in Use**
   - Change the port in configuration
   - Check for other running applications

2. **API Key Issues**
   - Verify API key is correct
   - Check API key permissions and credits

3. **Dependencies Issues**
   - Ensure all requirements are installed
   - Check Python version compatibility

4. **Memory Issues**
   - Increase memory allocation
   - Optimize application code

### **Support**:

- Check Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
- OpenAI API documentation: [platform.openai.com](https://platform.openai.com)
- Platform-specific documentation for your chosen deployment method

## **Cost Optimization**

1. **API Usage**
   - Monitor OpenAI API usage
   - Implement caching where possible
   - Use appropriate model sizes

2. **Infrastructure**
   - Choose appropriate instance sizes
   - Use auto-scaling when available
   - Monitor resource usage

3. **Bandwidth**
   - Optimize application size
   - Use CDN for static assets

---
**Note**: This deployment guide provides basic instructions. For production deployments, consider additional security, monitoring, and scaling requirements. 