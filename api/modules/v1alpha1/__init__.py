from typing import Dict

# TODO(nick): Auto-generate this from Go API models.

def extension_repo(
    name: str,
    labels: Dict[str, str] = None,
    annotations: Dict[str, str] = None,
    url: str = "",
    ref: str = ""):
  """
  ExtensionRepo specifies a repo or folder where a set of extensions live.

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    url: The URL of the repo.
      Allowed:
      https: URLs that point to a public git repo.
      file: URLs that point to a location on disk.
    ref: A reference to sync the repo to. If empty, Tilt will always update the repo to the latest version.
  """
  pass


def extension(
    name: str,
    labels: Dict[str, str] = None,
    annotations: Dict[str, str] = None,
    repo_name: str = "",
    repo_path: str = ""):
  """
  Extension defines an extension that's evaluated on Tilt startup.

  Args:
    name: The name in the Object metadata.
    labels: A set of key/value pairs in the Object metadata for grouping objects.
    annotations: A set of key/value pairs in the Object metadata for attaching data to objects.
    repo_name: RepoName specifies the ExtensionRepo object where we should find this extension.
	The Extension controller should watch for changes to this repo, and may update if
        this repo is deleted or moved.
    repo_path: RepoPath specifies the path to the extension directory inside the repo.
	Once the repo is downloaded, this path should point to a directory with a
	Tiltfile as the main "entrypoint" of the extension.
  """
  pass
