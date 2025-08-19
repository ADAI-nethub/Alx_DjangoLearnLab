# test_follow_feed.py
import requests
import json
import os
from django.test import TestCase
from django.contrib.auth import get_user_model

# For testing with live server (manual testing)
def manual_test_follow_feed():
    """Manual test script to run against your local development server"""
    BASE_URL = "http://localhost:8000/api"
    
    # You'll need to get these tokens by registering/login users first
    USER1_TOKEN = "replace-with-user1-actual-token"
    USER2_TOKEN = "replace-with-user2-actual-token"
    
    print("=== Testing Follow and Feed Functionality ===\n")
    
    # Test data - replace with actual user IDs from your database
    user1_headers = {"Authorization": f"Token {USER1_TOKEN}"}
    user2_headers = {"Authorization": f"Token {USER2_TOKEN}"}
    
    # User 1 follows User 2
    print("1. Testing follow functionality:")
    try:
        response = requests.post(f"{BASE_URL}/auth/users/2/follow/", headers=user1_headers)
        print(f"   Follow response: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # User 1 checks their feed
    print("\n2. Testing feed functionality:")
    try:
        response = requests.get(f"{BASE_URL}/posts/feed/", headers=user1_headers)
        print(f"   Feed response: {response.status_code}")
        if response.status_code == 200:
            feed_data = response.json()
            print(f"   Number of posts in feed: {len(feed_data.get('posts', []))}")
    except Exception as e:
        print(f"   Error: {e}")
    
    # User 1 checks who they're following
    print("\n3. Testing following list:")
    try:
        response = requests.get(f"{BASE_URL}/auth/me/following/", headers=user1_headers)
        print(f"   Following list: {response.status_code}")
        if response.status_code == 200:
            following = response.json()
            print(f"   Number of users followed: {len(following)}")
    except Exception as e:
        print(f"   Error: {e}")

if __name__ == "__main__":
    manual_test_follow_feed()