import React, { useState } from "react";

const Contact = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    message: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert("Thank you for contacting BeautyGlow! 💖");
    setFormData({ name: "", email: "", message: "" });
  };

  return (
    <section className="contact-page">
      <div className="container">
        {/* Hero */}
        <div className="contact-hero">
          <h1>Contact Us</h1>
          <p>
            We’re here to help you shine ✨  
            Reach out to us anytime with your questions or feedback.
          </p>
        </div>

        {/* Info Section */}
        <div className="contact-info">
          <div className="info-card">
            <h3>📍 Our Location</h3>
            <p>BeautyGlow HQ<br />Hyderabad, India</p>
          </div>

          <div className="info-card">
            <h3>📧 Email Us</h3>
            <p>support@beautyglow.com</p>
          </div>

          <div className="info-card">
            <h3>📞 Call Us</h3>
            <p>+91 98765 43210</p>
          </div>
        </div>

        {/* Form */}
        <div className="contact-form-wrapper">
          <h2>💌 Send Us a Message</h2>

          <form className="contact-form" onSubmit={handleSubmit}>
            <input
              type="text"
              name="name"
              placeholder="Your Name"
              value={formData.name}
              onChange={handleChange}
              required
            />

            <input
              type="email"
              name="email"
              placeholder="Your Email"
              value={formData.email}
              onChange={handleChange}
              required
            />

            <textarea
              name="message"
              placeholder="Your Message"
              rows="5"
              value={formData.message}
              onChange={handleChange}
              required
            />

            <button type="submit" className="btn btn-primary">
              ✨ Send Message
            </button>
          </form>
        </div>

        {/* Footer Text */}
        <div className="contact-footer">
          <h3>💖 We Value Your Voice</h3>
          <p>
            Your feedback helps us improve and bring you the best beauty
            experience possible.
          </p>
        </div>
      </div>
    </section>
  );
};

export default Contact;