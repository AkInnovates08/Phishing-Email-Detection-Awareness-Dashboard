from datetime import datetime, timezone
from sqlalchemy import DateTime, Float, Integer, String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database import Base

class Analysis(Base):
    __tablename__ = "analyses"

    analysis_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    sender_domain: Mapped[str] = mapped_column(String(255), default="")
    subject: Mapped[str] = mapped_column(String(500), default="")
    risk_score: Mapped[float] = mapped_column(Float, default=0)
    classification: Mapped[str] = mapped_column(String(80), default="LOW RISK")
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc).replace(tzinfo=None)
    )

    indicators = relationship(
        "Indicator", back_populates="analysis", cascade="all, delete-orphan"
    )
    urls = relationship(
        "URLAnalysis", back_populates="analysis", cascade="all, delete-orphan"
    )

class Indicator(Base):
    __tablename__ = "indicators"

    indicator_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    analysis_id: Mapped[int] = mapped_column(ForeignKey("analyses.analysis_id"))
    indicator_type: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(Text)
    severity: Mapped[str] = mapped_column(String(30))

    analysis = relationship("Analysis", back_populates="indicators")

class URLAnalysis(Base):
    __tablename__ = "url_analyses"

    url_analysis_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    analysis_id: Mapped[int] = mapped_column(ForeignKey("analyses.analysis_id"))
    url_safe_representation: Mapped[str] = mapped_column(Text)
    risk_score: Mapped[float] = mapped_column(Float, default=0)
    findings: Mapped[str] = mapped_column(Text, default="")

    analysis = relationship("Analysis", back_populates="urls")
