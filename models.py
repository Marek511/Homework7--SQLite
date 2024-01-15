from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    group_id = Column(Integer, ForeignKey("group.id"))

    group = relationship("Group", back_populates="students")
    grades = relationship("Grade", back_populates="student")


class Group(Base):
    __tablename__ = "group"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    students = relationship("Student", back_populates="group")


class Lecturer(Base):
    __tablename__ = "lecturer"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    subjects = relationship("Subject", back_populates="lecturer")


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    lecturer_id = Column(Integer, ForeignKey("lecturer.id"))

    lecturer = relationship("Lecturer", back_populates="subjects")
    grades = relationship("Grade", back_populates="subject")


class Grade(Base):
    __tablename__ = "grade"

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    subject_id = Column(Integer, ForeignKey("subject.id"))
    date = Column(DateTime)
    grade = Column(Integer)

    student = relationship("Student", back_populates="grades")
    subject = relationship("Subject", back_populates="grades")
