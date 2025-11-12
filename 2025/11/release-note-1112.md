
# Title: November 10, 2025 
Link: https://docs.cloud.google.com/release-notes#November_10_2025<br>
はい、承知いたしました。Google Cloudのリリースノートを元に、Compute Engineに関する既知のIssueについて、製品への影響有無と対処方法を調査し、以下の通りご回答します。

---

# Compute Engine
## Issue
原文:
The Windows guest agent identifies administrator accounts and groups using
string matching. Therefore, credential management features only function
correctly when you use English language names for user accounts and groups,
for example, `Administrators`. If you use non-English language names, credential
management features such as generating or resetting passwords might not function
as expected. For more information about managing Windows user accounts, see
[Manage accounts and credentials on Windows VMs](https://docs.cloud.google.com/compute/docs/instances/windows/generating-credentials) and
[Known issues for Windows VM instances](https://docs.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-non-english-credentials).

説明：
Compute EngineのWindows VMにインストールされているゲストエージェントは、管理者アカウントやグループを識別する際に、文字列の一致によって認識します。このため、パスワードの生成やリセットといった認証情報管理機能は、ユーザーアカウントやグループ名が英語名（例: `Administrators`）の場合にのみ、正しく動作します。もし、非英語の言語（例: 日本語の「管理者」）でアカウント名やグループ名を使用している場合、これらの認証情報管理機能が期待通りに動作しない可能性があります。

影響有無：
**影響あり**
もし貴社でCompute EngineのWindows VMインスタンスを利用しており、そのインスタンス内で管理者アカウントや管理者グループに英語以外の言語名（例: 日本語）を使用している場合、この既知のIssueの影響を受けます。具体的には、Google Cloud コンソールやgcloud CLIなどからWindows VMのパスワード生成やリセットを行おうとした際に、正しく処理が完了しない可能性があります。
Windows VMインスタンスを利用していない場合、または管理者アカウントやグループ名に常に英語名を使用している場合は、このIssueによる直接的な影響はありません。

対処方法：
現時点では、このIssueに対する修正パッチの提供ではなく、既知の問題として公開されています。認証情報管理機能が正しく動作するようにするためには、以下の対応を検討してください。

*   **アカウント名の英語化**: Windows VMの管理者アカウントおよびグループ名を、英語名（例: `Administrator`, `Administrators`）で設定してください。
*   **既存VMへの対応**: 既存のWindows VMで非英語の管理者アカウント名やグループ名を使用している場合、可能であれば英語名への変更を検討してください。変更が困難な場合は、Google Cloudの認証情報管理機能に依存せず、OS内部から直接パスワードを設定・管理するなど、代替の運用方法を検討する必要があります。
*   **ドキュメントの確認**: Google Cloudの公式ドキュメント「[Manage accounts and credentials on Windows VMs](https://docs.cloud.cloud.google.com/compute/docs/instances/windows/generating-credentials)」および「[Known issues for Windows VM instances](https://docs.cloud.cloud.google.com/compute/docs/troubleshooting/known-issues#windows-non-english-credentials)」で、より詳細な情報や最新の推奨事項を確認してください。

用語説明：
*   **Windows guest agent**: Compute EngineのWindows仮想マシン内で動作するソフトウェアで、VMとCompute Engineサービス間の連携を可能にします。パスワードのリセット、メタデータからの設定情報の取得、インスタンスの停止/再起動の制御など、様々な管理機能を提供します。
*   **Credential management features**: 認証情報管理機能のこと。Compute Engineでは、Windows VMのパスワードを生成したり、既存のパスワードをリセットしたりする機能が含まれます。これらはVMへのアクセス認証情報を安全に管理するために使用されます。
*   **String matching**: 文字列照合、または文字列マッチング。ここでは、特定のパターンや辞書に含まれる文字列と、入力された文字列を比較して識別する処理を指します。このIssueでは、ゲストエージェントが管理者アカウント名を特定する際に、固定の英語文字列（`Administrators`など）と照合していることを意味します。