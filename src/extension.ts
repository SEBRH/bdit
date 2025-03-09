import * as vscode from 'vscode';
import { exec } from 'child_process';
import * as fs from 'fs';

export function activate(context: vscode.ExtensionContext) {
    console.log('Congratulations, your extension "bdit" is now active!');

    const disposable = vscode.commands.registerCommand('bdit.generateComponent', () => {
        const pythonPath = vscode.Uri.joinPath(
            vscode.Uri.file(context.extensionPath),
            'src/untitled.py'
        ).fsPath;
        
        const pythonCmd = process.platform === "win32" ? "python" : "python3";
        const comando = `${pythonCmd} "${pythonPath}" template_sidebar --color azul`;

        vscode.window.showInformationMessage('WORKEANDO!' + comando);

        exec(comando, (error, stdout, stderr) => {
            if (error) {
                vscode.window.showErrorMessage(`Error: ${stderr}`);
                return;
            }

            vscode.window.showInformationMessage(`Salida generada correctamente.`);

            // Ruta del archivo de salida
            const mdFilePath = vscode.Uri.joinPath(
                vscode.workspace.workspaceFolders?.[0].uri || vscode.Uri.file(context.extensionPath),
                "output.md"
            );

            // Escribir la salida en el archivo
            fs.writeFile(mdFilePath.fsPath, stdout, (err) => {
                if (err) {
                    vscode.window.showErrorMessage(`Error al escribir archivo: ${err.message}`);
                    return;
                }

                // Abrir el archivo en el editor
                vscode.workspace.openTextDocument(mdFilePath).then((doc) => {
                    vscode.window.showTextDocument(doc);
                });
            });
        });
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
