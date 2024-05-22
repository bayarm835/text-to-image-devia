ARG PYTHON_BASE=3.9-slim
# build stage
FROM python:$PYTHON_BASE AS builder

# install PDM
RUN pip install -U pdm
# disable update check
ENV PDM_CHECK_UPDATE=false
# copy files
COPY pyproject.toml pdm.lock README.md /project/
COPY src/ /project/src

WORKDIR /project
RUN pdm install --check --prod --no-editable

# run stage
FROM python:$PYTHON_BASE

# retrieve packages from build stage
COPY --from=builder /project/.venv/ /project/.venv
ENV PATH="/project/.venv/bin:$PATH"
# set command/entrypoint, adapt to fit your needs
COPY src /project/src

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "project/src/text_to_image_devia/app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
