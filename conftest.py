import pytest
import os


@pytest.fixture(scope="function")
def page(context, request):
    trace_name = f"trace_{request.node.name}.zip"
    trace_path = os.path.join("traces", trace_name)

    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path=trace_path)
